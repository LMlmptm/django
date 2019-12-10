from django.contrib import admin
from booktest.models import AreaInfo
# Register your models here.

#块显示，显示城市下面所有的地区
class AreaStack(admin.StackedInline):
    model = AreaInfo
    extra = 2
#表显示  和上面一样的效果
class AreaTable(admin.TabularInline):
    model = AreaInfo
    extra = 2

class AreaRegister(admin.ModelAdmin):
    list_per_page = 10#限制每页显示多少行
    list_display = ['id','atitle','aparent']
    list_filter = ['aparent']#过滤器右边
    actions_on_top = False#表示上面框不显示
    actions_on_bottom = True#表示下面框显示
    search_fields = ['atitle']#寻找框上边
    #fields = ['aparent','atitle']#上下颠倒
    #和上面差不多，下面实现的是块装饰，和上面不能同时存在
    fieldsets = (
        ('基本',{'fields':['atitle']}),
        ('高级',{'fields':['aparent']})
    )
    inlines = [AreaStack]
   # inlines=[AreaTable]

admin.site.register(AreaInfo,AreaRegister)