# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import os

from django.db import models


# Create your models here.
def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (datetime.datetime.now(), ext)
    return os.path.join('IMAGE/', filename)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, max_length=50)
    parent = models.CharField(blank=True, max_length=50)
    is_featured = models.BooleanField(default=False)
    image = models.FileField(upload_to=user_directory_path, null=True)
    is_active = models.BooleanField(default=False)
    description = models.CharField(default="No Description", max_length=150)
    users = models.ForeignKey('usermgmt.Users', related_name='categories', on_delete=models.CASCADE, null=False)

    class Meta:
        ordering = ('id', 'name', 'is_featured',)
