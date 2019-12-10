from django.db import models

# Create your models here.

class AreaInfo(models.Model):
    #verbose_name可以用其他名称来显示在admin后台
    atitle=models.CharField(max_length=40,verbose_name="地区")
    aparent=models.ForeignKey('self',null=True,blank=True,verbose_name='城市',on_delete=models.CASCADE)

    def __str__(self):
        return self.atitle

    #这个也是可以实现和上面一样的功能
    # def title(self):
    #     return self.atitle
    #排序
    # title.admin_order_field='atitle'
    # title.short_description='城市'
