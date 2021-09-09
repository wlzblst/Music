from django.shortcuts import render
from index.models import *
from django.views.generic import ListView


def rankingView(request):
    # 热搜歌曲
    search = Dynamic.objects.select_related('song').order_by('-search').all()[:4]
    # 歌曲分类列表
    labels = Label.objects.all()
    # 歌曲列表信息
    t = request.GET.get('type', '')
    if t:
        dynamics = Dynamic.objects.select_related('song').filter(song__label=t).order_by('-plays').all()[:10]
    else:
        dynamics = Dynamic.objects.select_related('song').order_by('-plays').all()[:10]
    return render(request, 'ranking.html', locals())


class RankingList(ListView):
    # 设置模板的某个变量名称
    context_object_name = 'dynamics'
    # 设置模板文件
    template_name = 'ranking.html'

    # 设置变量dynamics的数据
    def get_queryset(self):
        # 获取请求参数
        t = self.request.GET.get('type', '')
        if t:
            dynamics = Dynamic.objects.select_related('song').filter(song__label=t).order_by('-plays').all()[:10]
        else:
            dynamics = Dynamic.objects.select_related('song').order_by('-pages').all()[0:10]
        return dynamics

    # 添加变量
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 搜索歌曲
        context['search'] = Dynamic.objects.select_related('song').order_by('-search').all()[:4]
        # 所有歌曲分类
        context['labels'] = Label.objects.all()
        return context

# Create your views here.
