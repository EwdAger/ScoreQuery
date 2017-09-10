# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import jwc_spider, models

# Create your views here.

def w_data():
    spider = jwc_spider.spider()
    data = spider.query_spider()      #返回字典
    models.Score.objects.create(stu_id=data.stu_id, name=data.name, class_num=data.class_num,
                                major=data.major, c_name=data.c_name, term=data.term,
                                c_type=data.c_type, score=data.score, credit=data.credit,
                                properties=data.properties)

