#! /usr/bin env python3
# -*- coding:utf-8 -*-
from post.models import *
from django.db.models import *
from datetime import date


# slider context
def slider_context_processor(request):
    # information about slider needed
    content = dict()
    content['category'] = Post.objects.values('category','category__name').annotate(count=Count('*'))

    archive = Post.objects.values('createdTime').order_by('-createdTime')
    content['archive'] = archive
    content['recent'] = Post.objects.order_by('-createdTime').all()[:5]

    # print('执行')
    return content
