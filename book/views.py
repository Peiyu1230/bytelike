from django.shortcuts import render
from django.http import HttpResponse
from book.models import *

# Create your views here.

def creat(request):
    BookInfo.objects.create(
        name = '西游记',
        pub_data='2020-1-1',
        read_count=100,
        comment_count=100
    )
    return HttpResponse("creat")
def shop(request,city_id,shop_id):
    # print(city_id,shop_id)
    qurey = request.GET
    # order = qurey.get('order')
    # order = qurey['order']
    # 一键多值
    order=qurey.getlist('order')
    print(order)
    return HttpResponse("商城列表")
def register(request):
    data = request.POST
    print(data)
    return HttpResponse("ok")