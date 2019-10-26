import datetime
import json
import os

from alipay import AliPay
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse
from django_redis import get_redis_connection

# from market.models import Goods
from .models import Order,OrderDetail
from contents.models import Goods
# from orders.models import Order, OrderDetail
from users.models import User


def index(request):
    #生成订单逻辑
    #1.获取购物车的数据,从redis中取数据
    username = request.session.get('username')
    redis_cli  = get_redis_connection('cart')
    cart_data = json.loads(redis_cli.get(f'cart-{username}'))

    # 判断redis中商品的选中状态:
    cart_dict ={}
    for cart in cart_data:
        if cart_data[cart]['selected'] =="1":
            #{'gid':'count1",'gid2':'count2'}
            cart_dict[int(cart)] = int(cart_data[cart]['count'])
    #生成订单总信息
    user = User.objects.get(username=username)
    #生成订单号:'20190923141414+uid'
    order_code = int(datetime.datetime.now().strftime('%Y%m%d%H%M%S')+str(user.id))

    order = Order.objects.create(
        uid=user.id,
        order_code=order_code,
        total_count=sum(cart_dict.values()),
        total_amount=0,
        status=0

    )
    totalcount = 0
    #4,生成子订单:
    for gid,count in cart_dict.items():
        #先判断库存够不够
        good = Goods.objects.get(productid=gid)
        if count > good.storenums:
            return HttpResponse('商品库存不足')

        #减库存加销量
        good.storenums = good.storenums-count
        good.productnum = good.productnum+count

        good.save()
        #生成子订单
        OrderDetail.objects.create(
            uid=user.id,
            order_code=order_code,
            goods_id=gid,
            counts=count,
            price=good.price

        )
        totalcount +=good.price*count
        #清除选中商品的 redis数据
        del cart_data[str(gid)]

    order.total_amount = totalcount
    order.save()
    #重新添加redis数据
    redis_cli.set(f'cart-{username}',json.dumps(cart_data))
    # context={
    #     'order':order,
    #
    # }

    return redirect(reverse('orders:order'))


def orderdetail(request,order_code):
    username = request.session.get('username')
    user = User.objects.get(username=username)
    uid = user.id
    orderdetail= OrderDetail.objects.filter(order_code=order_code,uid=uid)
    data_list = []

    for data in orderdetail:
        goods = Goods.objects.get(productid=data.goods_id)
        data_dict ={
           'id': goods.productid,
           'img': goods.productimg,
           'name': goods.productname,
           'price': goods.price,
           'count':data.counts
       }
        data_list.append(data_dict)

    context = {
        'data_list':data_list
    }

    return render(request,'orderdetail.html',context)


def order(request):
    if request.session.get('username'):
        username = request.session.get('username')
        user = User.objects.get(username=username)
        uid = user.id
        order = Order.objects.filter(uid=uid,status=0)
        print(order)
        context={
            'orders':order
        }
        return render(request,'order.html',context)
    return redirect(reverse('users:login'))

def pay(request,order_code):
    alipay = AliPay(
        appid='2016101100663220',
        app_notify_url=None,  # 默认回调url
        app_private_key_path=os.path.join(settings.BASE_DIR, "alipay/app_private_key.pem"),
        alipay_public_key_path=os.path.join(settings.BASE_DIR, "alipay/alipay_public_key.pem"),
        sign_type="RSA2",
        debug=True
    )

    order = Order.objects.get(order_code=order_code)

    # 生成登录支付宝连接
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no=order_code,
        total_amount=float(order.total_amount),
        subject='商品支付信息',
        return_url='http://127.0.0.1:8000/payback/',
    )

    alipay_url = 'https://openapi.alipaydev.com/gateway.do?' + order_string
    return redirect(alipay_url)


def payback(request):
    query_dict = request.GET
    data = query_dict.dict()

    # 获取并从请求参数中剔除signature
    signature = data.pop('sign')

    # 创建支付宝支付对象
    alipay = AliPay(
        appid='2016101100663220',
        app_notify_url=None,  # 默认回调url
        app_private_key_path=os.path.join(settings.BASE_DIR, "alipay/app_private_key.pem"),
        alipay_public_key_path=os.path.join(settings.BASE_DIR, "alipay/alipay_public_key.pem"),
        sign_type="RSA2",
        debug=True
    )
    # 校验这个重定向是否是alipay重定向过来的
    success = alipay.verify(data, signature)
    if success:
        order_code = data['out_trade_no']
        Order.objects.filter(order_code=order_code).update(status=1)
        return redirect(reverse('orders:unreceive'))
    else:
        # 验证失败
        return HttpResponse('支付失败')


def unreceive(request):
    username = request.session.get('username')
    user = User.objects.get(username=username)
    uid = user.id
    order = Order.objects.filter(uid=uid, status=1)
    print(order)
    context = {
        'orders': order
    }
    return render(request, 'unreceive.html', context)
