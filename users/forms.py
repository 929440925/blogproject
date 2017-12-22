from django import forms

# from captcha.fields import CaptchaField
from captcha.fields import CaptchaField

from .models import UserProfile

class LoginForm(forms.Form):    #登录验证
    username = forms.CharField(required=True)   #验证不能为空，必填
    password = forms.CharField(required=True,min_length=5)


class RegisterForm(forms.Form):     #注册验证
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=5)
    captcha = CaptchaField(error_messages={'invalid':u'验证码错误'})    #图片验证码相关

class ForgetForm(forms.Form):     #注册验证
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid':u'验证码错误'})    #图片验证码相关

class ModifyPwdForm(forms.Form):     #注册验证
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)

