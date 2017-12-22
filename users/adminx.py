# -*- coding:utf-8 -*-
__author__ = 'jummy'

import xadmin
from xadmin import views
from .models import EmailVerifyRecord

class BaseSetting(object):  #样式设置
    enable_themes = True    #开启主题功能
    use_bootswatch = True    #


class GlobalSetting(object):    #针对所有的修改
    site_title = '后台管理系统' #左上角标题修改
    site_footer = 'Jummy'   #底部公司名称修改




xadmin.site.register(views.BaseAdminView,BaseSetting)   #主题注册
xadmin.site.register(views.CommAdminView,GlobalSetting) #针对所有的修改