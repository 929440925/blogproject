# -*- coding:utf-8 -*-
__author__ = 'jummy'

from django.conf.urls import url


from .views import AddCommentView

urlpatterns = [
    #url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
    url(r'add_comment/$',AddCommentView.as_view(),name='addcomment'),
]

