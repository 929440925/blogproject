# -*- coding:utf-8 -*-
__author__ = 'jummy'

import xadmin
from .models import Tag, Post, Category


class CategoryAdmin(object):
    list_display = ['name'] #字段显示
    search_fields = ['name']    #搜索
    list_filter = ['name']  #筛选


class TagAdmin(object):
    list_display = ['name']  # 字段显示
    search_fields = ['name']  # 搜索
    list_filter = ['name']  # 筛选


class PostAdmin(object):
    list_display = ['title','body','created_time','modified_time','excerpt','views','category','tags','author']  # 字段显示
    search_fields = ['title','body','excerpt','views','category','tags','author']  # 搜索
    list_filter = ['title','body','created_time','modified_time','excerpt','views','category','tags','author']  # 筛选
    style_fields = {'body':'ueditor'}  # 对自定义的插件进行识别


xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Tag,TagAdmin)
xadmin.site.register(Post,PostAdmin)