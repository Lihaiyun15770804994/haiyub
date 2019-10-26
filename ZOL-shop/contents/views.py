from django.http import HttpResponse
from django.shortcuts import render
from . import models

# Create your views here.


def show(request):
    login = False
    username = request.session.get('username')
    if username:
        login = True
    wheel = models.Goods.objects.all()
    context = {
        'wheels':wheel,
        'login':login,
        'username':username
    }
    return render(request,'mainPage.html',context)


def detail(request,id):
    login = False
    username = request.session.get('username')
    if username:
        login = True
    details = models.Goods.objects.get(productid=id)
    context = {
        'details': details,
        'login':login,
        'username':username
    }
    return render(request,'proPage1.html',context)