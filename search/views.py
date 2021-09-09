from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.shortcuts import reverse
from django.db.models import Q,F
from index.models import *
def searchView(request,page):
    if request.method == 'GET':
        #热搜歌曲
        search = Dynamic.objects.select_related('song').order_by('-search').all()[:6]
        #获取搜索内容，若为空则查询所有歌曲
        kwords = request.session.get('kword','')
        if kwords:
            #Q是SQL语句里的or语法,icontains相当于模糊查询
            songs = Song.objects.filter(Q(name__icontains=kwords)|Q(singer=kwords)).order_by('-release').all()
        else:
            songs = Song.objects.order_by('-release').all()[:50]
        #分页功能
        paginator = Paginator(songs,5)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        #添加歌曲搜索次数
        if kwords:
            idList = Song.objects.filter(name__icontains=kwords)
            for i in idList:
                #判断歌曲动态信息是否存在，若存在，则在原来的基础上加1
                dynamics = Dynamic.objects.filter(song_id=i.id)
                if dynamics:
                    dynamics.update(search=F('search')+1)
                else:
                    dynamic = Dynamic(plays=0,search=1,download=0,song_id=i.id)
                    dynamic.save()
        return render(request,'search.html',locals())
    else:
        #处理POST请求，并重定向搜索页面,重定向相当于向歌曲搜索页发送一个GET请求
        request.session['kword'] = request.POST.get('kword','')
        return redirect(reverse('search',kwargs={'page':1}))


# Create your views here.
