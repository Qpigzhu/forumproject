from django.shortcuts import render
from django.shortcuts import render
from userforum.models import Forum,SowingMap
# Create your views here.


def index(request):
    all_forum = Forum.objects.all()
    all_sowing_map = SowingMap.objects.all()
    return render(request, 'index.html', {
        'all_forum': all_forum,
        'all_sowing_map':all_sowing_map,
    })