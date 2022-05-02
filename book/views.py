from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest
from django.http import HttpResponse

def index(request):
    # return HttpResponse("OK")

    # 模拟数据
    context ={
        'name':'有惊喜 快来参加!'
    }
    return render(request,'book/index.html',context=context)