from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from article.models import ArticlePost


def article_list(request):
    articles = ArticlePost.objects.all()
    content = {'article':articles}
    return render(request, 'article/list.html', content)

# 文章详情
# 实现了文章详情页面。为了让文章正文能够进行标题、加粗、引用、代码块等不同的排版（像在Office中那样！），这里使用Markdown语法。
# Markdown是一种轻量级的标记语言，它允许人们“使用易读易写的纯文本格式编写文档，然后转换成有效的或者HTML文档。
import markdown
def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)
    # 将markdown语法渲染成html样式
    article.body = markdown.markdown(article.body,
        extensions=[
            # 包含 缩写、表格等常用扩展
            'markdown.extensions.extra',
            # 语法高亮扩展
            'markdown.extensions.codehilite',

        ])
    content = {'article':article}
    return render(request, 'article/detail.html', content)


# 写文章的视图
from article.form import ArticlePostForm
from django.shortcuts import redirect
def article_create(request):
    # 对请求的类型进行判断
    if request.method == 'POST':
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存数据，暂时不提交数据库
            new_article = article_post_form.save(commit=False)
            # 指定数据库中id=1的用户为作者
            new_article.author = User.objects.get(id=1)
            # 将新文章保存到数据库中
            new_article.save()
            # 完成后返回文章列表
            return redirect('article:article_list')
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 如果用户请求获数据
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 赋值上下文
        context = {'article_post_form': article_post_form}
        # 返回模板
        return render(request, 'article/create.html', context)

# 删除文章
def article_delete(request, id):
    article = ArticlePost.objects.get(id=id)
    article.delete()
    return redirect("article:article_list")

def article_update(request, id):
    """
    更新文章的视图函数
    通过post方法提交表单，更新title,body字段
    GET方法进入初始表单页面
    id：文章的id
    """
    article = ArticlePost.objects.get(id=id)

    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(data=request.POST)

        if article_post_form.is_valid():
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            return redirect("article:article_detail",id=id)
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    else:
        article_post_form = ArticlePostForm()

        context = {'article':article,'article_post_form':article_post_form}

        return render(request,'article/update.html', context)