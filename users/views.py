from django.shortcuts import render
from django.views.generic.base import View
from django.core.urlresolvers import reverse
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q  #并级（和）
from django.contrib.auth.hashers import make_password   #对明文加密
from utils.email_send import send_register_email
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect


from .forms import LoginForm, RegisterForm
from .models import UserProfile,EmailVerifyRecord
# Create your views here.


class CustomBackend(ModelBackend):  #自定义登录验证,添加Email登录方式
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))  #可以使用用户名和Email登录
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):  #以类视图方式登录验证
    def get(self,request):
        return render(request,'users/login.html')
    def post(self,request):
        longn_form = LoginForm(request.POST)
        if longn_form.is_valid():
            user_name = request.POST.get('username', '')    #获取输入的用户名，默认为空
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)  # 向服务器验证用户名和密码是否正确
            if user is not None:
                if user.is_active:
                    login(request,user)  # 完成登录
                    return HttpResponseRedirect(reverse('blog:index'))
                else:
                    return render(request, 'users/login.html', {'msg': '用户未激活'})
            else:
                return render(request, 'users/login.html', {'msg': '用户名或密码错误！'})
        else:
            return render(request, 'users/login.html', {'login_form':longn_form})


class LogoutView(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse('blog:index'))


class RegisterView(View):   #注册
    def get(self,request):
        register_form = RegisterForm()
        return render(request,'users/register.html',{'register_form':register_form})

    def post(self,request):
        register_form = RegisterForm(request.POST)  #初始化表单
        if register_form.is_valid():
            user_name = request.POST.get('email','')
            if UserProfile.objects.filter(email=user_name):
                return render(request,'users/register.html',{'register_form':register_form,'msg':"用户已存在"})
            pass_word = request.POST.get('password','')
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)    #加密保存
            user_profile.save()

            send_register_email(user_name,'register')
            return render(request, 'users/login.html')
        else:
            return render(request, 'users/register.html',{'register_form':register_form})


class ActiveUserView(View): #发送注册邮件
    def get(self,request,active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, 'users/active_fail.html')
        return render(request, 'users/login.html')



