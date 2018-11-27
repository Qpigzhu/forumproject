from django.shortcuts import render,redirect
from django.urls import reverse #直接传入url
from django.views import View
from django.http import JsonResponse
from django.contrib import auth
from .forms import LoginForm,RegisteredForm
# Create your views here.

class LoginView(View):
    def get(self,request):
        login_form = LoginForm()
        return render(request, 'login_or_registered.html',{
            'login_form': login_form,
        })
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)#和数据库账号密码是否相同
        if user is not None:#有此用户
            auth.login(request, user)

            return JsonResponse({"code":"200"})

        else:
            return JsonResponse({"code":"201"})

#注册
class RegisteredView(View):
    def get(self, request):
        registered_form = RegisteredForm()
        return render(request, 'login_or_registered.html',{
            'registered_form': registered_form,
        })
    def post(self, request):
        pass



