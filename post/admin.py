# -*- coding:utf-8 -*-
from django.contrib import admin

from django.contrib import admin
from post.models import *
# Register your models here.


# control how to display post in background admin interface
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'createdTime', 'category']
    # list_display_links = ['content']
    list_filter = ['category', 'createdTime']
    # search box
    search_fields = ['tags__name']
    list_per_page = 5
    # use JavaScript interface rather than check box to manage ManytoManyField
    filter_horizontal = ['tags']


# register model to active in background interface
admin.site.register(Post, PostModelAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(About)
