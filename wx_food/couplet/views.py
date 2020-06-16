# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from subprocess import check_output
import socket
# Create your views here.
# 渲染登录首页
def main_view(request):
    uname = request.GET.get('up_couplet','')
    if not uname:
        return render(request, "couplet/main.html")
    else:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("localhost", 9000))
        sock.send(uname.encode("utf-8"))
        result = sock.recv(1024).decode(encoding="utf-8")
        result = result.split("\n")[-2]
        result = ''.join(result.split(" "))
        result = uname + "，" + result
    return render(request, "couplet/index.html", locals())

# 处理登录功能
def index_view(request):
    # 接收请求参数
    uname = request.GET.get('up_couplet','')

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 9000))
    sock.send(uname.encode("utf-8"))
    result = sock.recv(1024).decode(encoding="utf-8")
    print(result)

    # 判断
    #if len(uname)!=0:  #判断输入成功的条件 我先设置只要输入不为空即可
    return render(request,'couplet/index.html', locals())

