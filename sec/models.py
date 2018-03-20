# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    blog_user = models.ForeignKey(User)
    content = models.TextField(null=False)
    direction = models.CharField(max_length=30)
    url = models.CharField(max_length=100)
    time = models.CharField(max_length=30)
    week = models.IntegerField()
    def __unicode__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.content