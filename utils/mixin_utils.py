# -*- coding: utf-8 -*-
# @Time    : 2017/5/16 20:39
# @Author  : yj

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class LoginRequiredMixin(object):

    #login_required判断用户是否登录
    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self,request,*args,**kwargs):
        return super(LoginRequiredMixin,self).dispatch(request,*args,**kwargs)