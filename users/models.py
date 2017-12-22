# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

#用户
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50,verbose_name=u'昵称',default='')   #昵称
    birday = models.DateField(verbose_name=u'生日',null=True,blank=True)  #生日
    gender = models.CharField(max_length=6,choices=(('male',u'男'),('female','女')),default='male') #性别
    address = models.CharField(max_length=100,default=u'')  #地址
    mobile = models.CharField(max_length=11,null=True,blank=True)   #电话
    image = models.ImageField(upload_to='image/%Y/%m',default=u'image/default.png',max_length=100)  #头像

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


#邮箱验证码
class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name=u'验证码')
    email = models.CharField(max_length=50,verbose_name=r'邮箱')
    send_type = models.CharField(verbose_name=u'验证码类型',choices=(("register",u"注册"),("forget",u"找回密码"),("update_email",u"修改邮箱")),max_length=20)
    send_time = models.DateTimeField(verbose_name=u'发送时间',default=datetime.now)

    class Meta:
        verbose_name = u'邮箱验证码'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code,self.email)
