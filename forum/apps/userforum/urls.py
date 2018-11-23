# _*_ encoding:utf-8 _*_
__author__ = 'pig'
__data__ = '2018\11\22 0022 10:30$'

from django.urls import path
from .views import ForumView

urlpatterns = [
    path('',ForumView.as_view(),name="forum_datil"),
]