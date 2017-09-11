# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Score(models.Model):
    stu_id = models.CharField(max_length=200, verbose_name='学号')
    name = models.CharField(max_length=200, verbose_name='姓名')
    grade = models.CharField(max_length=200, verbose_name='年级')
    class_num = models.CharField(max_length=200, verbose_name='班级')
    major = models.CharField(max_length=200, verbose_name='专业')

    c_name = models.CharField(max_length=200, verbose_name='课程名')
    term = models.CharField(max_length=200, verbose_name='开课学期')
    c_type = models.CharField(max_length=200, verbose_name='课程性质')

    score = models.CharField(max_length=200, verbose_name='成绩')
    credit = models.CharField(max_length=200, verbose_name='学分')
    properties = models.CharField(max_length=200, verbose_name='考试性质')


    class Meta:
        verbose_name = u'学生成绩'
        verbose_name_plural = u'学生成绩'

    def __unicode__(self):
        return self.name