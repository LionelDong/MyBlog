# -*- coding:utf-8 -*-

from django.conf.urls import url
from post import views

# The `urlpatterns` list routes URLs to views.
urlpatterns = [
    url(r'^$', views.index_view, name='index_view'),
    url(r'^page/(\d+)$', views.index_view, name='index_view'),
    url(r'^post/details/(\d+)$', views.post_details_view, name='post_details_view'),
    url(r'^about/', views.about_view, name='about_view'),
    url(r'^category/(\d+)$', views.category_details_view, name='categery_details_view'),
    url(r'^archive/(\d+)/(\d+)$', views.date_details_view, name='date_details_view'),
    url(r'^archive/', views.date_details_view, name='date_details_view'),
    url(r'^tag/(\d+)', views.tag_details_view, name='tag_details_view'),
    url(r'^search/$',views.search_view, name='search_view')
]