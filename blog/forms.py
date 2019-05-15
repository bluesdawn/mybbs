#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 15:03
# @Author  : Wq
# @File    : forms.py
# @Software: PyCharm

from django import forms
from django.core.exceptions import ValidationError
from blog import models
class RegForm(forms.Form):
    username = forms.CharField(
        label='用户名',
        min_length=4,
        widget=forms.widgets.TextInput(
            attrs={"class": "form-control"},
        ),
        error_messages={
            'required':'不能为空',
            'min_length':'用户名最短4',
        }
    )

    password = forms.CharField(
        label='密码',
        min_length=6,
        widget=forms.widgets.PasswordInput(
            attrs={"class": "form-control"},
            render_value=True
        ),
        error_messages={
            'required': '不能为空',
            'min_length': '密码最短6',
        }
    )

    re_password = forms.CharField(
        label='确认密码',
        min_length=6,
        widget=forms.widgets.PasswordInput(
            attrs={"class": "form-control"},
            render_value=True
        ),
        error_messages={
            'required': '不能为空',
            'min_length': '密码最短6',
        }
    )

    email = forms.EmailField(
        label='邮箱',
        widget=forms.widgets.EmailInput(
            attrs={"class": "form-control"},
        ),
        error_messages={
            "invalid": "邮箱格式不正确！",
            "required": "不能为空",
        }
    )
    #重写局部钩子
    def clean_username(self):
        username = self.cleaned_data.get('username')
        ret = models.UserInfo.objects.filter(username=username)
        if ret:
            self.add_error('username', ValidationError("用户名已存在"))
        else:
            return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        ret = models.UserInfo.objects.filter(email=email)
        if ret:
            self.add_error('email', ValidationError("邮箱已存在"))
        else:
            return email

    #from django.core.exceptions import ValidationError
    # 重写全局的钩子函数，对确认密码做校验
    def clean(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if re_password and re_password != password:
            self.add_error('re_password',ValidationError("两次密码不一致"))
        else:
            return self.cleaned_data

