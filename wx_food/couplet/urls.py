#coding=utf-8


from django.conf.urls import url

from wx_food import settings
from . import views
from django.views.static import serve

urlpatterns=[
    url(r'^static/', views.index_view),
    url(r'^login/', views.login_view),
    ]