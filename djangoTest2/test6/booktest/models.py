from django.db import models


class BookInfo(models.Model):
    #图书名称
    btitle=models.CharField(max_length=30)
    bpub_date=models.DateField()
    bread=models.IntegerField(default=0)
    bcomment=models.IntegerField(default=0)
    isDelete=models.BooleanField(default=False)



class HeroInfo(models.Model):
    #英雄名称
    hname=models.CharField(max_length=40)
    #性别
    hgender=models.BooleanField(default=False)
    hcomment=models.CharField(max_length=300,null=True,blank=True)
    hbook=models.ForeignKey('BookInfo',on_delete=models.CASCADE)
    isDelete=models.BooleanField(default=False)



#自己和自己关联在一起
class AreaInfo(models.Model):
    #设置地区名称
    atitle=models.CharField(max_length=30)
    #设置自关联
    aparent=models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE)


