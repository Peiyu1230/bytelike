from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
# Create your views here.

def index(request):

    return HttpResponse("ok")


##################1、添加数据#######################
from book.models import *

# 1\方法
book = BookInfo(
    name = '红楼梦',
    pub_data='2020-1-1',
    read_count = 10
)
book.save()

# 2方案
BookInfo.objects.create(
    name = '三国演义',
    pub_data='2020-1-1',
    read_count = 10
)

##################2\更新数据#######################

# 1、方法1
book = BookInfo.objects.get(id=6)
book.name = "运维开发"
book.save()

# 2、方法2
BookInfo.objects.filter(id=6).update(name="水浒传",pub_data="2022-05-01")

##################3\删除数据#######################

# 1\方法1
book = BookInfo.objects.get(id=8)
book.delete()

# 2、方法2
BookInfo.objects.get(id=8).delete()
# or
BookInfo.objects.filter(id=8).delete()