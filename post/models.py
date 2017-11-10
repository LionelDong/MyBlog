# -*- coding:utf-8 -*-
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


# Category of post
class Category(models.Model):
    name = models.CharField(max_length=60, unique=True)

    # display the name of category in background control interface
    def __str__(self):
        return u'%s'%self.name


# tags of post
class Tag(models.Model):
    name = models.CharField(max_length=60, unique=True)

    # display the name of tag in background control interface
    def __str__(self):
        return u'%s'%self.name


# post manager
class PostManager(models.Manager):

    # add tags to post
    def create_add_tags(self, title, category, tags, createdTime, modifiedTime, content):
        # self current manager
        post = self.create(
            title=title,
            category=category,
            createdTime=createdTime,
            modifiedTime=modifiedTime,
            content=content
        )
        post.tags.add(*tags)
        post.save()

    # post query method by keywords
    def query_post_by_keywords(self,keyword):
        return self.filter(title__contains=keyword).order_by('-title')

    # display all post and sort by created time
    def all(self):
        return super(models.Manager, self).all().order_by('-created')


# post
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    createdTime = models.DateField(auto_now_add=True, verbose_name='创建时间')
    modifiedTime = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    category = models.ForeignKey(Category, verbose_name='类别')
    tags = models.ManyToManyField(Tag, verbose_name='标签')

    # display the title of post in background control interface
    def __str__(self):
        return u'%s'%self.title

    # Meta information in form
    class Meta():
        verbose_name_plural = '博文'


# about me
class About(models.Model):
    username = models.CharField(max_length=20, unique=True,default='demon')
    desc = RichTextUploadingField()

    # display the information in backend
    def __str__(self):
        return u'%s'%self.username

