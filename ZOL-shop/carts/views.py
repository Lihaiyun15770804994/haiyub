import json

from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.

from django.urls import reverse
from django_redis import get_redis_connection

from contents.models import Goods


def index(request):
    # login = False
    if not request.session.get('username'):
        return redirect(reverse('users:login'))

    #1.从cookie里取出数据
    username = request.session.get('username')
    login =True

    redis_cli = get_redis_connection('cart')
    data = redis_cli.get(f'cart-{username}')


    totalprice = 0
    data_list = []
    #2.先判断cookie里有没有数据
    if data:
        #2.把字符串转成字典
        data = json.loads(data)


        #3.通过商品的id,把商品的数据取出来
        for d in data:
            # 查数据
            goods = Goods.objects.get(productid = d)
            # 把需要用到的数据组装成字典格式

            data_dict = {
                'id':goods.productid,
                'img':goods.productimg,
                'name':goods.productname,
                'price':goods.price,
                'num':data[d]['count'],
                'selected':data[d]['selected'],
            }
            print(data_dict)
            print(data[d]['count'])
            allprice = goods.price*int(data[d]['count'])
            data_dict['allprice']=allprice
            if data[d]['selected']=='1':
                totalprice+= goods.price*int(data[d]['count'])
            data_list.append(data_dict)


    context ={
        'data_list':data_list,
        'totalprice':totalprice,
        'login':login,
        'username':username
    }


    return render(request,'cart.html',context)
    # return render(request,'cart.html',context)


def selects(request):
    selected = request.POST.get('selected')

    username = request.session.get('username')

    redis_cli = get_redis_connection('cart')
    cookie_data = redis_cli.get(f'cart-{username}')


    cookie_data = json.loads(cookie_data)

    for data in cookie_data:
        cookie_data[data]['selected']=selected
    cookie_data = json.dumps(cookie_data)

    res =JsonResponse({'data':'ok'})

    redis_cli.set(f'cart-{username}',cookie_data)

    return res

def savedata(request):
    # 1.获取数据
    gid = request.POST.get('gid')
    print(gid)
    count = request.POST.get('count')
    print(count)
    selected = request.POST.get('selected','1')

    #如果登录,数据就存储到redis里面
    # if request.session.get('username'):
    #     username = request.session.get('username')
        #数据在redis里面应该怎么存
        #确定存储的格式就是字典形式的字符串
        #1.实例化 redis对象
    username = request.session.get('username')
    redis_cli = get_redis_connection('cart')
        #2.获取redis购物车数据
    cookie_data = redis_cli.get(f'cart-{username}')
    # else:
    #     cookie_data = request.COOKIES.get('cookie_data')

    #存在一个问题,如果cookie里面有数据,需要存在相同的数据,需要覆盖
    # 如果不存在,需要添加
    # 先把cookie_data的值查出啦
    # cookie_data = request.COOKIES.get('cookie_data')

    if cookie_data:
        # print(gid)
        cookie_data = json.loads(cookie_data)
        #如果cookie_data含有gid的数据就覆盖,如果没有就新增
        cookie_data[gid] = {'count':count,'selected':selected}

    else:
        # 2.把数据组装成格式为:
        # {‘商品的id':{'count':'商品的数量','selected':'商品选中的状态'}
        # 放入cookie中
        cookie_data = {gid: {'count': count, 'selected': selected}}


    if count == '0':
        # print(cookie_data)
        del cookie_data[gid]
    cookie_data = json.dumps(cookie_data)
    res = JsonResponse({'data': 'ok'})
    # if request.session.get('username'):
    redis_cli.set(f'cart-{username}',cookie_data)
    # else:
    # 3.cookie里面只能放字符串,所以需要把字典格式转成字符串

        # res.set_cookie('cookie_data',cookie_data)
    return  res


def delete(request):
    gid = request.POST.get('gid')
    username = request.session.get('username')
    redis_cli = get_redis_connection('cart')
    # 2.获取redis购物车数据
    cookie_data = redis_cli.get(f'cart-{username}')
    cookie_data=json.loads(cookie_data)
    del cookie_data[gid]
    cookie_data = json.dumps(cookie_data)
    res = JsonResponse({'data': 'ok'})
    redis_cli.set(f'cart-{username}', cookie_data)
    return res