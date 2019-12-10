from django.contrib import admin

from booktest.models import BookInfo, HeroInfo, AreaInfo


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bread', 'bcomment', 'isDelete']


class HeroAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'hgender', 'hcomment', 'isDelete', 'hbook']


class AreaAdmin(admin.ModelAdmin):
    list_display = ['atitle', 'aparent']


admin.site.register(BookInfo, BookAdmin)
admin.site.register(HeroInfo, HeroAdmin)
admin.site.register(AreaInfo, AreaAdmin)
