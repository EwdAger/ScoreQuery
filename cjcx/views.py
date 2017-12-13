# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import jwc_spider
import json
# Create your views here.

def login(request):
    return render(request, 'login.html')

def check(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    spider = jwc_spider.spider()
    msg = spider.score_spider(username, password)
    if msg != '':
        return render(request, 'login.html', {
            "msg": json.dumps(msg)
        })
    datas, years = spider.score_data()
    sorted(years)
    print(years)
    return render(request, 'index.html', {
        "datas": datas,
        "years": years
    })