from django.shortcuts import render
from django.views import View
from .models import Forum
# Create your views here.

class ForumView(View):
    def get(self,request):
        return render(request,'info.html',{

        })

