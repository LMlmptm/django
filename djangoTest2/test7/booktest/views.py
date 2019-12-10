from django.shortcuts import render

# Create your views here.

def index(request):
    # meta=request.META['REMOTE_ADDR']#获取浏览器的ip
    # print(meta)
    print("index")
    #a='a'+1
    return render(request,'booktest/index.html',{})