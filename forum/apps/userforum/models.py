from django.db import models
from user.models import UserProfile
# Create your models here.

class ForumType(models.Model):
    type_name = models.CharField(max_length=20,verbose_name="帖子类型")
    add_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "帖子类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.type_name



class Forum(models.Model):
    author = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name="发帖作者")
    title = models.CharField(max_length=15,verbose_name="标题")
    comment = models.TextField(verbose_name="帖子内容")
    forum_type = models.ForeignKey(ForumType,on_delete=models.CASCADE,verbose_name="帖子类型")
    add_time = models.DateTimeField(auto_now_add=True,verbose_name="发帖时间")


    class Meta:
        verbose_name = "帖子"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title



