# -*- coding: utf-8 -*-

from django.http import HttpResponse

from myapps.models import Test

import urllib.parse as urlparse
from django.shortcuts import render,HttpResponse,redirect
from django.views import View

def detail(request):
    user_list = [{"username":22,"id":1,"path":"go"},{"username":223,"id":2,"path":"go"}]
    return render(request, 'detail.html', {'user_list': user_list})

#从url字符串中获取指定参数值
def getUrl(url):
    url = 'http://test.laozhang.com/h5/nsx/#/autoLogin?code=9bc8096d-8be0-40ef-9cd1-8b7624d5f063&redirect_url=/?umentData=%7B%22umengEventId%22:%22PageInsurance%22,%22umengParams%22:%7B%22Source%22:%22btn_bxfw_td%22%7D%7D'
    #排除干扰项字符
    url = url.replace("#/autoLogin", "")
    parsed = urlparse.urlparse(url)
    querys = urlparse.parse_qs(parsed.query, True)
    print(querys)
    return HttpResponse(querys['code'])

# 数据库操作
def testdbadd(request):
    test1 = Test(name='hello world')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")


def testdbquery(request):
    # 初始化
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Test.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = Test.objects.filter(id=1)

    # 获取单个对象
    response3 = Test.objects.get(id=1)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    Test.objects.order_by('name')[0:2]

    # 数据排序
    Test.objects.order_by("id")

    # 上面的方法可以连锁使用
    Test.objects.filter(name="runoob").order_by("id")

    # 输出所有数据
    for var in list:
        response1 += var.name + " <br />"
    response = response1
    return HttpResponse("<p>" + response + "</p>")
