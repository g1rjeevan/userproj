# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from category.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent', 'is_featured', 'is_active', 'description', 'users')


admin.site.register(Category, CategoryAdmin)
