# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Post(models.Model):

    title = models.CharField(max_length=50,unique=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="blog_posts")
    slug = models.SlugField(max_length=200,unique=True)
    date_created = models.DateTimeField(auto_now=True)
    last_modified = models.DateField(auto_now=True)
    content = models.TextField()
    category = models.ManyToManyField("Category",related_name="posts")
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

class Comment(models.Model):

    author = models.CharField(max_length=50)
    date_created = models.DateField(auto_now=True)
    content = models.TextField()
    post = models.ForeignKey("Post",on_delete=models.CASCADE)


