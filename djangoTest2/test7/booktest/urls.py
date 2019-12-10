from django.urls import re_path
from booktest import views
urlpatterns = [
    re_path(r'^index$',views.index),#展示 图片man.jpg
   ]
