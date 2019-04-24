# 引入path
from django.urls import path

# 正在部署的应用的名称
from article import views

app_name = 'article'

urlpatterns = [
    # 目前还没有urls
    path('article-list/', views.article_list, name='article_list'),
    # 文章详情
    path('article-list/<int:id>/', views.article_detail, name='article_detail'),
    # 写文章
    path('article-create/', views.article_create, name='article_create'),
    # 删除文章
    path('article-delete/<int:id>/', views.article_delete, name='article_delete'),
    # 更改文章
    path('article-update/<int:id>/', views.article_update, name='article_update'),
]