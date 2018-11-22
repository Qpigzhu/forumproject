# _*_ encoding:utf-8 _*_
__author__ = 'pig'
__data__ = '2018\11\21 0021 22:08$'

import xadmin
from .models import ForumType,Forum

class ForumTypeAdmin(object):
    list_dispaly = ['type_name','add_time']
    search_fields = ['type_name']
    list_filter =['type_name','add_time']


class ForumAdmin(object):
    list_dispaly = ['author','title','comment','forum_type','add_time']
    search_fields = ['author','title','comment','forum_type']
    list_filter =['author','title','comment','forum_type','add_time']

xadmin.site.register(ForumType,ForumTypeAdmin)
xadmin.site.register(Forum,ForumAdmin)