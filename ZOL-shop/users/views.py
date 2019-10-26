import random
import re

from django.contrib.auth.hashers import check_password, make_password
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
import requests
from django.urls import reverse
from django_redis import get_redis_connection


from users.models import User


def login(request):
    if request.method =="POST":
        #1.接收参数
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)



        #2.判断参数
        user = User.objects.filter(username=username)
        if not user.exists():
            return HttpResponse('用户不存在')

        if not check_password(password,user[0].password):
            return HttpResponse('密码错误')


        #处理逻辑
        #保存用户的登录状态
        request.session['username'] = username

        # cookie_to_redis(request)
        #4.返回响应
        return redirect(reverse('contents:show'))
        # cookie_to_redis(request,res)

        # return cookie_to_redis(request,res)

    else:
        return render(request,'login.html')



def register(request):
    if request.method =="POST":
        username = request.POST.get('txt')
        password = request.POST.get('pwd')
        # 2判断参数
        # 判断用户名不能重复
        usernm1 = re.search('^\w{8,11}$',username)
        usernm2 = re.search('^\w+?@\w+?.com',username)
        usernm = re.search('^1[3578]\d{9}$',username)
        passwd = re.search('^\w{8,11}$',password)
        if  usernm2 or usernm or usernm1:
            pass
        else:
            return HttpResponse('用户名不合法')#如果用户名不符合要求返回响应
        if not passwd:
            return HttpResponse('密码输入不合法')#如果密码不符合要求

        res =User.objects.filter(username=username).exists()

        if res:
            return HttpResponse('用户名已存在')

        User.objects.create(
            username=username,
            password=make_password(password),

        )
        # 4,返回响应
        return redirect(reverse('users:login'))

    # RESTful
    # API由后台也就是SERVER来提供前端来调用。前端调用API向后台发起HTTP请求，后台响应请求将处理结果反馈给前端。


    return render(request,'register.html')


def sendsms(request):
    # 用云之讯第三方发短信
    phone = request.POST.get('phone')
    smscode = random.randint(1000,9999)
    data = {
        "sid": "8036ece41e07ea5340794286185f9214",
        "token": "8a9c9099eb825ea314bcb620f9fdbc6b",
        "appid": "cceff1236cee4e1e87b87186dc10ad27",
        "templateid": "493813",
        "param": smscode,
        "mobile": phone,
    }
    res = requests.post('https://open.ucpaas.com/ol/sms/sendsms',json=data)
    res = res.json()
    print(res)
    if res['code'] =='000000':
        # 保存验证码,保存在缓存里面,给一个过期时间
        # 实例化redis
        redis_cli = get_redis_connection()
        redis_cli.set('sms'+phone,smscode,60)
        return JsonResponse({'res':'ok'})
    else:
        return JsonResponse({'res':'no'})


def logout(request):
    del request.session['username']
    return redirect(reverse('contents:show'))