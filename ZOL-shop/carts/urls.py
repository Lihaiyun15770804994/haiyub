from django.conf.urls import url

from carts import views

urlpatterns = [
    url(r'^cart/$',views.index,name='index'),
    url(r'^selects/$',views.selects,name='selects'),
    url(r'^savedata/$',views.savedata,name='savedata'),
    url(r'^del/$',views.delete,name='delete'),
]