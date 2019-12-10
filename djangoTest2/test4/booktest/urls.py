from django.urls import re_path

from booktest import views

urlpatterns = [
    re_path(r'^index2$', views.index,name='index'),  # 首页
    re_path(r'^temp_var$', views.temp_var),  # 测试模板变量
    re_path(r'^temp_tags$', views.temp_tags),  # 模板标签
    re_path(r'^temp_filter$', views.temp_filter),  # 模板过滤器
    re_path(r'^temp_inherit$', views.temp_inherit),  # 模板继承
    re_path(r'^temp_myfilter$', views.temp_myfilter),  # 自定义过滤器
    re_path(r'^login_check$', views.login_check),
    re_path(r'^login$', views.login),
    re_path(r'^change_pwd$',views.change_pwd),#修改密码
    re_path(r'^change_pwd_action$',views.change_pwd_action),#修改密码并返回
    re_path(r'^verify_code$',views.verify_code),#生成验证码
    re_path(r'^url_reverse$',views.url_reverse),#验证url反向解析
    re_path(r'^url_reverses/(\d+)/(\d+)$',views.url_reverses,name='url_re'),#带参数的url反向解析
    re_path(r'^view_reverse$',views.view_reverse),#视图层的反向解析
]
