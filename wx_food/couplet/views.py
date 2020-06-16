# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from subprocess import check_output
import socket
# Create your views here.
# 渲染登录首页
def index_view(request):

    return render(request,'couplet/login.html',locals())

# 处理登录功能
def login_view(request):
    # 接收请求参数
    uname = request.GET.get('shang','')

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 9000))
    sock.send(uname.encode("utf-8"))
    result = sock.recv(1024).decode(encoding="utf-8")
    print(result)

    # 判断
    # if len(uname)==0:  #判断输入成功的条件 我先设置只要输入不为空即可
    return render(request,'couplet/fail.html')


    # return render(request,'couplet/login.html')