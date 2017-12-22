# -*- coding:utf-8 -*-
__author__ = 'jummy'

from django.conf.urls import url

from .views import IndexView,PostDetailView,ArchivesView,CategoryView,TagView,love


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', PostDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', TagView.as_view(), name='tag'),
    #url(r'^search/$', search, name='search'),
    url(r'^love/$',love,name='love'),
]