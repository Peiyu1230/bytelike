from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
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
    print(city_id,shop_id)
    # 方法2
    # qurey = request.GET
    # order = qurey.get('order')
    # order = qurey['order']

    # 一键多值
    # order=qurey.getlist('order')
    # print(order)
    return HttpResponse("商城列表")
def register(request):
    data = request.POST
    print(data)
    return HttpResponse("ok")
#############
import json
def jsons(request):
    data = request.body
    data_str = data.decode()
    body = json.loads(data_str)
    print(body)
    return HttpResponse('json')

def res(request):
    info = {
        'name':'jack',
        'address':'changpong',
    }
    girl_list = [
        {
            'name': 'jack',
            'address': 'changpong',
        },
        {
            'name': 'nick',
            'address': 'haidian',
        }
    ]
    response = JsonResponse(girl_list,safe=False)

    return response


################ cookie 和 session ###############

def set_cookie(request):
    username = request.GET.get('username')

    response = HttpResponse("set_cookie")

    response.set_cookie('name',username)

    return response

def get_cookie(request):
    name = request.COOKIES.get('name')
    return HttpResponse(name)