#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 引入表单类
from django import forms
# 引入 User 模型
from django.contrib.auth import models
from django.contrib.auth.models import User

# 登录表单，继承了 forms.Form 类
from userprofile.models import Profile


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()



# 注册用户表单类
# 对数据库进行操作表单应该继承forms.ModelForm，自动生成模型中已有的字段
class UserRegisterForm(forms.ModelForm):
    # 复写User的密码
    password = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email')

    #对两次输入密码的一致性进行判断
    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password2'):
            return data.get('password')
        else:
            raise forms.ValidationError("密码输入不一致，请重试。")



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone','avater','bio')