from django.shortcuts import render,get_object_or_404
from django.views import View

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Forum,ForumType


# Create your views here.

#
class ForumView(View):
    def get(self,request):
        all_forum = Forum.objects.all()
        forum_count  = all_forum .count()
        forum_type = ForumType.objects.all()

        #分页插件
        try:
            #获取前端页数
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        #进行分页处理
        p = Paginator(all_forum,7,request=request)

        #取出分页页数数据
        forum = p.page(page)

        return render(request,'list.html',{
            "all_forum":forum,
            "all_forum_type":forum_type,
            "forum_count":forum_count,
        })

#详情页面
class ForumDatileView(View):
    def get(self, request,forum_id):
        forum = get_object_or_404(Forum,id=forum_id)
        return render(request, 'info.html', {
            "forum":forum,
        })