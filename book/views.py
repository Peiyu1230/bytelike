from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import View

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

################ session ###############

def set_session(request):
    username = request.GET.get('username')
    request.session['user_id'] = 1
    request.session['username'] = username
    return HttpResponse("set_session")

def get_sesion(request):
    user_id = request.session.get('user_id')
    username = request.session.get('username')
    context = '{},{}'.format(user_id,username)

    return HttpResponse(context)

# 类视图

class login(View):
    def get(self,request):
        return HttpResponse('get get get')
    def post(self,request):
        return HttpResponse('post post post')

# 多继承

from django.contrib.auth.mixins import LoginRequiredMixin

# 多继承遵循mro规则
# 必须有admin页面的登录信息才可以正常return
class OrderView(LoginRequiredMixin,View):
    def get(self,request):
        return HttpResponse('Get 我的订单页面')
    def post(self,request):
        return HttpResponse('Post 我的订单页面')