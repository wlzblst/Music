from django.shortcuts import render, redirect, reverse
from index.models import *
from user.models import *
from .form import MyUserCreationForm
from django.db.models import Q
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def loginView(request):
    # user为由表单生成的注册表单
    user = MyUserCreationForm()
    if request.method == 'POST':
        if request.POST.get('loginUser', ''):
            u = request.POST.get('loginUser', '')
            p = request.POST.get('password', '')
            if MyUser.objects.filter(Q(mobile=u) | Q(username=u)):
                u1 = MyUser.objects.filter(Q(mobile=u) | Q(username=u)).first()
                if check_password(p, u1.password):
                    login(request, u1)
                    return redirect(reverse('home', kwargs={'page': 1}))
                else:
                    tips = '密码错误'
            else:
                tips = '用户不存在'
        # 用户注册
        else:
            u = MyUserCreationForm(request.POST)
            if u.is_valid():
                u.save()
                tips = '注册成功'
            else:
                if u.errors.get('username', ''):
                    tips = u.errors.get('username', '注册失败')
                else:
                    tips = u.errors.get('mobile', '注册失败')
    return render(request, 'user.html', locals())


# 用户中心
# 设置用户登陆限制
@login_required(login_url='/user/login.html')
def homeView(request, page):
    # 热搜歌曲
    search = Dynamic.objects.select_related('song').order_by('-search').all()[:4]
    # 分页功能
    songs = request.session.get('play_list', [])
    paginator = Paginator(songs, 3)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(page)
    except EmptyPage:
        page = paginator.page((paginator.num_pages))
    return render(request, 'home.html', locals())


def logoutView(request):
    logout(request)
    return redirect('/')

# Create your views here.
