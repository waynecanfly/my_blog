# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# 博客文章数据模型
class ArticlePost(models.Model):
    # on_delete用于指定数据删除的方式
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 保存较短的字符使用CharField
    title = models.CharField(max_length=100)
    # 保存大量文本使用TextField
    body = models.TextField()
    # 文章创建时间，参数default=timezone.now指定其在创建数据时将默认写入当前的时间
    created = models.DateTimeField(default=timezone.now)
    # 文章更新时间。参数auto_now=True指定每次数据更新时自动写入当前的时间
    updated = models.DateTimeField(auto_now=True)

    # 内部类 Meta用于给model定义元数据
    class Meta:
        # ording指定模型返回的数据的排列顺序
        # '-created'表明数据应该已倒序排列
        ordering = ('-created',)
    # 定义调用str()方法时返回的值内容
    def __str__(self):

        return self.title