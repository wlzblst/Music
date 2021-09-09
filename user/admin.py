from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from  django.utils.translation import gettext_lazy as _

@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ['username','email','mobile','qq','weChat']
    #在用户修改页面添加字段
    fieldsets = list(UserAdmin.fieldsets)
    #重写UserAdmin的fieldsets,添加字段
    fieldsets[1] = (_('Personal info'),{'fields':('first_name','last_name','email','mobile','qq','weChat')})
# Register your models here.
