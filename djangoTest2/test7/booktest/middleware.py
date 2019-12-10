from django.http import HttpResponse

class BlockedIPSMiddleware(object):
    def process_view(self,request,view_func,*view_args,**view_kwargs):
        user_ip=request.META['REMOTE_ADDR']#获取访问的浏览器的ip
        print(user_ip)
        return HttpResponse("中间件")


class TestDemo(object):
    #首先调用init初始化方法,这个方法只会被调用一次，初始化的时候调用
    def __init__(self,request):
        print("调用init")
    #然后调用这个函数
    def process_request(self,request):
        print("调用process_request")
       #在views.py之前调用，然后返回给views.py
    def process_view(self,request,view_func,*view_args,**view_kwargs):
        print("调用Process_views")
    #结束的时候调用，在views.py之后
    def process_response(self,request,response):
        print("调用process_response")
        return response

class ExceptionMiddle(object):
    def process_exception(self,request,exception):
        print("process_exception1")

class Exception2Middle(object):
    def process_exception(self,request,exception):
        print("process_exception2")
