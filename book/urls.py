from django.urls import path
from book.views import *
from django.urls import converters
from django.urls.converters import register_converter

class MobileConverter:
    regex = '1[3-9]\d{9}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)
# 注册
register_converter(MobileConverter,"mobile")

urlpatterns = [
    path('creat/', creat),
    path('<int:city_id>/<mobile:shop_id>/',shop),
    path('register/',register),
    path('json/',jsons),
    path('res/',res),
    path('set_cookie/',set_cookie),
    path('get_cookie/',get_cookie),
    path('set_session/',set_session),
    path('get_session/',get_sesion),
#     类视图
    path('163login/',login.as_view()),
    path('order/',OrderView.as_view())
]