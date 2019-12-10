from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.template import loader, RequestContext
from django.urls import reverse
from booktest.models import BookInfo


# Create your views here.
def index(request):
    # 定义加载模板文件
    temp = loader.get_template('booktest/index.html')
    # 导入模板文件,加载数据
    context = RequestContext(request, {})
    context.push(locals())
    # 渲染模板文件
    render_html = temp.render(context=locals(), request=request)
    return HttpResponse(render_html)


# 测试模板变量 可以是字典，列表和对象
def temp_var(request):
    my_dict = {"btitle": "man"}
    my_list = [1, 23, 4]
    book = BookInfo.objects.get(id=1)
    context = {"my_dict": my_dict, "my_list": my_list, "book": book}
    return render(request, 'booktest/temp_var.html', context)


# 模板标签
def temp_tags(request):
    books = BookInfo.objects.all()
    return render(request, 'booktest/temp_tags.html', {'books': books})


# 模板过滤器filter
def temp_filter(request):
    books = BookInfo.objects.all()
    return render(request, 'booktest/temp_filter.html', {'books': books})


# 模板继承
def temp_inherit(request):
    return render(request, 'booktest/child.html', {})


# 自定义模板过滤器
def temp_myfilter(request):
    list = [1, 6, 3, 9, 8, 2]
    temp = loader.get_template('booktest/temp_myfilter.html')
    context = RequestContext(request, {'list': list})
    context.push(locals())
    render_html = temp.render(context=locals(), request=request)
    return HttpResponse(render_html)

#装饰器 主要是用来判断是不是在线状态
def login_required(func):
    def loginTest(request,*args,**kwargs):
        if  request.session.has_key('islogin'):
            return func(request,*args,**kwargs)
        else:
            return redirect('/login')
    return loginTest

def login(request):
    if request.session.has_key('islogin'):
        return redirect('/change_pwd')
    else:
        if 'username' in request.COOKIES:
            username = request.COOKIES['username']
        else:
            username = ''
        return render(request, 'booktest/login.html', {'username': username})


def login_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    code1=request.POST.get('code1')#这个时用户输入的验证码
    print(code1)
    code2=request.session.get('verifycode')#这个时存储在session里面的验证码
    print(code2)
    if code1 != code2:
        return redirect('/login')

    if username == 'man' and password == '123':
        response = redirect('/change_pwd')
        if remember == 'on':
            response.set_cookie('username', username, max_age=2 * 24 * 3600)
        request.session['islogin'] = True
        request.session['username']=username#获取session的用户名，永久保存
        return response
    else:
        return redirect('/login')

  #修改密码
@login_required
def change_pwd(request):
    return render(request,'booktest/change_pwd.html',{})
#修改密码返回
@login_required
def change_pwd_action(request):
    #获取修改密码后的密码并返回
    pwd=request.POST.get('pwd')
    username=request.session.get('username')#通过session获得的
    return HttpResponse("%s修改密码后为:%s"%(username,pwd))

#验证码生成
from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO
def verify_code(request):
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高 RGB
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)

    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]

    # 构造字体对象，ubuntu的字体路径为“C:\Users\MACHENLKE\Desktop\djangoTest2\FreeMono.ttf”
    font = ImageFont.truetype(r'C:\Users\MACHENLKE\Desktop\djangoTest2\FreeMono.ttf', 23)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    print(rand_str)
    request.session['verifycode'] = rand_str
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')

#url反向解析
def url_reverse(request):
    return render(request,'booktest/url_reverse.html',{})

#url反向解析带参数
def url_reverses(request,a,b):
    return HttpResponse(a+b)

#视图层的反向解析，其他带参数的参考上面或者上网搜，args,kwargs都是针对带参数的
def view_reverse(request):
    url=reverse('booktest:index')
    return redirect(url)