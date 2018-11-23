from django.shortcuts import render,get_object_or_404
from django.views import View
from .models import Forum
# Create your views here.

#
# class ForumView(View):
#     def get(self,request):
#
#         return render(request,'info.html',{
#
#         })

#详情页面
class ForumDatileView(View):
    def get(self, request,forum_id):
        forum = get_object_or_404(Forum,id=forum_id)
        return render(request, 'info.html', {
            "forum":forum,
        })