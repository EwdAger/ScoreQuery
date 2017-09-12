# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import models
import jwc_spider

# Create your views here.

def w_data():
    spider = jwc_spider.spider()
    data_list = spider.query_spider()      #返回字典列表
    for data in data_list:
        if not models.Score.objects.filter(c_name=data['c_name'], properties=data['properties']).exists():
            models.Score.objects.create(stu_id=data['stu_id'], name=data['name'], class_num=data['class_num'],
                                        major=data['major'], c_name=data['c_name'], term=data['term'],
                                        c_type=data['c_type'], score=data['score'], credit=data['credit'],
                                        properties=data['properties'], grade=data['grade'],
                                        point=data['point'], grade_point=data['grade_point']
                                        )

def class_rank(request):
    pass

def index(request):
    w_data()
    return render(request, 'index.html', locals())
