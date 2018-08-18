# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from usermgmt.models import Users

admin.site.register(Users, UserAdmin)

admin.site.unregister(Group)