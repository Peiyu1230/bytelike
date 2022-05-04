from django.urls import path
from book.views import *

urlpatterns = [
    path('creat/', creat),
    path('<city_id>/<shop_id>/',shop),
    path('register/',register),
]