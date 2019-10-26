from django.conf.urls import url

from contents import views

urlpatterns = [
    url(r'^show1/$', views.show, name='show'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),

]