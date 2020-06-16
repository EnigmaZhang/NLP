# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from subprocess import check_output
import socket
import re
import string
# Create your views here.
# 渲染登录首页
def main_view(request):
    error_string = "欢迎使用智能生成对联系统，请输入七个及以下简体汉字"
    cn_punc = "！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏."
    punc_pattern = re.compile("[{}{}]".format(cn_punc, string.punctuation))
    uname = request.GET.get('up_couplet','')
    if not uname:
        return render(request, "couplet/main.html")
    elif not re.match("[\u4e00-\u9fa5]+", uname):
        result = error_string
    elif len(uname) > 7:
        result = error_string
    elif punc_pattern.search(uname):
        result = error_string
    else:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(("localhost", 9000))
            sock.send(uname.encode("utf-8"))
            result = sock.recv(1024).decode(encoding="utf-8")
            result = result.split("\n")[-2]
            result = ''.join(result.split(" "))
            result = uname + "，" + result
        except ConnectionRefusedError:
            result = "服务器存在问题，请稍候再试"
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

    return render(request,'couplet/index.html', locals())

