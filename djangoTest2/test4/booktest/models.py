from django.db import models


# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=30)
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.btitle


class HeroInfo(models.Model):
    hname = models.CharField(max_length=60)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=80)
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.hname


class AreaInfo(models.Model):
    # 设置地区名称
    atitle = models.CharField(max_length=30)
    # 设置自关联
    aparent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
