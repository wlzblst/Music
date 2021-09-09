from django.shortcuts import render
from .models import *
def indexView(request):
    #通过外建‘song’关联两个模型的数据
    songDynamic = Dynamic.objects.select_related('song')
    #热搜歌曲
    searchs = songDynamic.order_by('-search').all()[:8]
    #音乐分类
    labels = Label.objects.all()
    #热门歌曲
    popular = songDynamic.order_by('-plays').all()[:10]
    #新歌推荐
    recommend = Song.objects.order_by('release').all()[:3]
    #热门搜索，热门下载
    downloads = songDynamic.order_by('-download').all()[:6]
    #将searchs和downloads的数据放置到同一个列表中
    tabs = [searchs[:6],downloads]
    return render(request,'index.html',locals())

def page_not_found(request,exception):
    return render(request,'404.html',status=404)

def page_error(request):
    return render(request,'404.html',status=500)
# Create your views here.
