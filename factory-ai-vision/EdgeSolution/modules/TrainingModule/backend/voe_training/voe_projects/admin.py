# -*- coding: utf-8 -*-
"""App admin."""

from django.contrib import admin

from .models import Project

# Register your models here.
admin.site.register(Project)
