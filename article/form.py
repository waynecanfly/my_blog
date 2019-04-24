#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django import forms

# 写文章的表单类
from article.models import ArticlePost


class ArticlePostForm(forms.ModelForm):
    class Meta:
        # 指明数据模型的来源
        model = ArticlePost
        # 定义表单包含的字段
        fields = ('title', 'body')