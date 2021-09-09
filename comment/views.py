from django.shortcuts import render,redirect,reverse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import Http404
from index.models import *
import time

def commentView(requset,id):
    #热搜歌曲
    search = Dynamic.objects.select_related('song').order_by('-search').all()[:6]
    #点评内容的提交功能
    if requset.method == 'POST':
        text = requset.POST.get('comment','')
        #如果用户处于登陆状态就是用用户名，否则使用匿名用户
        if requset.user.username:
            user = requset.user.username
        else:
            user = '匿名用户'
        now = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        if text:
            comment = Comment()
            comment.text = text
            comment.user = user
            comment.date = now
            comment.song_id = id
            comment.save()
        return redirect(reverse('comment',kwargs={'id':str(id)}))
    else:
        songs = Song.objects.filter(id=id).first()
        #如果歌曲不存在
        if not songs:
            raise Http404
        else:
            c = Comment.objects.filter(song_id=id).order_by('date')
            page = int(requset.GET.get('page',1))
            paginator = Paginator(c,2)
            try:
                pages = paginator.page(page)
            except PageNotAnInteger:
                pages =paginator.page(1)
            except EmptyPage:
                pages = paginator.page(paginator.num_pages)
            return render(requset,'comment.html',locals())

# Create your views here.
