#! /usr/bin env python3
# -*- coding:utf-8 -*-
from haystack import indexes
from post.models import *


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    # set index to post title and content
    title = indexes.CharField(model_attr='title')
    content = indexes.CharField(model_attr='content')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.order_by('-createdTime').all()