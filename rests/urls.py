from django.conf.urls import url
from .views import home,api

urlpatterns =[
    url(r'^rest/$',home,name='home'),
    url(r'^api/$',api,name='api'),
]
