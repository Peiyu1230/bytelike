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


##################4\查询数据(单个查询)#######################


# get获取单个和全部数据
BookInfo.objects.get(id=1)
BookInfo.objects.all()
# 获取数据数量
BookInfo.objects.all().count()
BookInfo.objects.count()

##################4\查询数据(过滤查询)#######################

# 查询编号等于1的商品
book = BookInfo.objects.get(id=1)
book = BookInfo.objects.get(id__exact=1)

# filter获取到的是列表 get获取到的是数值
book = BookInfo.objects.filter(id=1)

# id也可以写成pk primary key 主键
book = BookInfo.objects.get(pk=1)


# 查询输名字包含"xx"的图书
BookInfo.objects.filter(name__contains="传")
# 查询书名以""结尾的图书
BookInfo.objects.filter(name__endswith="传")
# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)
# 查询编号为1、3、5的图书
BookInfo.objects.filter(id__in=[1,3,5])
# 查询编号大于3的图书
BookInfo.objects.filter(id__gt=5)
# 查询编号大于等于3的图书
BookInfo.objects.filter(id__gte=3)
# 查询编号小于3的图书
BookInfo.objects.filter(id__lt=3)
# 查询编号小于等于3的图书
BookInfo.objects.filter(id__lte=3)
# 查询编号不等于3的图书
BookInfo.objects.exclude(id=1)
# 查询1980年以后的图书
BookInfo.objects.filter(pub_data__year__gt="2020")
# 查询2000年发布的图书
BookInfo.objects.filter(pub_data__year="2000")

##############两个数据的比较F##########################
from django.db.models import F

# 获取阅读量大于等于评论量的数据

BookInfo.objects.filter(read_count__lte=F('commit_count'))

############## 并&非~查询 ##########################
from django.db.models import Q

# 查询阅读量大于20并且编号小于3的书籍

BookInfo.objects.filter(read_count__gte=10,id__lt=3)
BookInfo.objects.filter(read_count__gte=10).filter(id__lt=3)
BookInfo.objects.filter(Q(read_count__gte=10)&Q(id__lt=3))

# 查询阅读量大于20或者编号小于3的书籍
BookInfo.objects.filter(Q(read_count__gte=10)|Q(id__lt=3))

# 查询id不等于3的数据
BookInfo.objects.filter(~Q(id=1))

