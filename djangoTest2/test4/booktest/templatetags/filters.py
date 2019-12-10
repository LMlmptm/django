from django.template import Library

# 实例化自定义过滤器
register = Library()


# filter为自定义名字，要在网页中调用这个名字
@register.filter(name="filter")
def mod(num):
    return num % 2 == 0
