from django.urls import path
from .views import *
urlpatterns = [
    #用户注册和登陆
    path('login.html',loginView,name='login'),
    #用户注册
    path('home/<int:page>.html',homeView,name='home'),
    #退出用户登录
    path('logout.html',loginView,name='logout'),
]