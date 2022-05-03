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