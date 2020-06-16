#coding=utf-8


from django.conf.urls import url

from wx_food import settings
from . import views
from django.views.static import serve

urlpatterns=[
    url(r'^main/', views.main_view),
    url(r'^index/', views.index_view),
    ]