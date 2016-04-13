# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from verify.tasks import send_verify_email

class SignupForm(forms.Form):

    username = forms.CharField(label='username', max_length=100,
                              widget=forms.TextInput(attrs={'class': 'TK_input'}), error_messages={
                                  'required': u'请输入用户名',
                                  'invalid': u'无效的用户名',

                              })
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'Tk_input', 'max_length': 75}),
                            error_messages={
                                'required': u'请输入邮箱',
                                'invalid': u'无效的邮箱',
                            }
                           )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'Tk_input', 'max_length': 30}),
                             error_messages={
                                 'required': u'请输入密码',
                                 'invalid': u'密码应该是大于6位的字母数字_.组合',
                             })
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'Tk_input', 'max_length': 30}),
                             error_messages={
                                 'required': u'请输入密码',
                                 'invalid': u'密码应该是大于6位的字母数字_.组合',
                             })

    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        if '@' in username:
            raise forms.ValidationError(u'非法用户名')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password', '')
        return password
    
    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        return email

    def clean(self):
        username = self.clean_username()
        password = self.clean_password()
        email = self.clean_email()
        
        if '' in (username, password, email):
            raise forms.ValidationError(u'无效的验证')

        if not any(item in email for item in ['qq.com', '163.com']):
            raise forms.ValidationError(u'目前只支持163.com, qq.com 邮箱')

        #验证用户名有效性
        repeat_email = False
        try:
            email = User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            pass
        else:
            print u'邮箱已经注册'
            raise forms.ValidationError(u'邮箱已注册')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            print u'创建新用户'
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            #send email
            send_verify_email.delay(user.email, user.pk)
        else:
            print u'用户名已存在'
            raise forms.ValidationError(u'用户名已存在')


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=100,
                              widget=forms.TextInput(attrs={'class': 'TK_input'}), error_messages={
                                  'required': u'请输入用户名',
                                  'invalid': u'无效的用户名',

                              })
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'Tk_input', 'max_length': 30}),
                             error_messages={
                                 'required': u'请输入密码',
                                 'invalid': u'密码应该是大于6位的字母数字_.组合',
                             })

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password', '')
        return password

    def clean(self):
        username = self.clean_username()
        password = self.clean_password()
        
        if '' in (username, password):
            raise ValidationError(u'无效的用户')

        if '@' in username:
            try:
                email_user = User.objects.get(email__iexact=username, password=password)
            except User.DoesNotExist:
                pass
            else:
                self.user_cache = email_user
        
        if self.user_cache is None:
            username = user_name
        else:
            username = email_user.username

        user = authenticate(username=username, password=password)
        if user is None:
            raise ValidationError(u'用户名不存在或密码错误')
        else:
            self.user_cache = user

    def get_user(self):
        return self.user_cache





