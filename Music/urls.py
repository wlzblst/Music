"""Music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #首页
    path('',include('index.urls')),
    #排行榜
    path('ranking.html',include('ranking.urls')),
    #播放页面
    path('play/',include('play.urls')),
    #评论页面
    path('comment/',include('comment.urls')),
    #搜索
    path('search/',include('search.urls')),
    #用户
    path('user/',include('user.urls')),
    #定义媒体资源的路由信息
    re_path('media/(?P<path>.*)',serve,{'document_root':settings.MEDIA_ROOT},name='media'),
    #定义静态资源的路由信息
    re_path('static/(?P<path>.*)',serve,{'document_root':settings.STATIC_ROOT},name='static'),
]

from index import views
handle404 = views.page_not_found
handle500 = views.page_error

