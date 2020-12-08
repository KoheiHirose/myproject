#// myapp/urls.py
 
from django.urls import path
from django.conf.urls import url
from . import views
 
app_name='myapp'
 
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # index.htmlにアクセスが来た場合、views.pyのindex関数の処理をする。

    url(r'^welcome/$', views.welcome, name='welcome'),
    url(r'^like/$', views.like, name='like'),
    url(r'^dislike/$', views.dislike, name='dislike'),
    url(r'^birthday/$', views.birthday, name='birthday'),
]