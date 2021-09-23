# -*- coding: utf-8 -*-

from django.http import HttpResponse


def getUserName(request):
    name = request.GET.get("name")
    return HttpResponse('姓名：{}'.format(name))
