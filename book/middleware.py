from django.utils.deprecation import MiddlewareMixin


class testMiddleWare(MiddlewareMixin):
    def process_request(self,request):
        print("每次请求前 都会调用")
    def process_response(self,request,response):
        print("每次响应前 都会调用")
        return response