from django.conf.urls import url

from orders import views

urlpatterns = [
    url(r'^orders/$',views.index,name='index'),
    url(r'^orderdetails/(\d+)/$',views.orderdetail,name='orderdetail'),
    url(r'^order/$',views.order,name='order'),
    url(r'^alipay/(\d+)/$',views.pay,name='alipay'),
    url(r'^payback/$',views.payback,name='payback'),
    url(r'^unreceive/$',views.unreceive,name='unreceive'),
]