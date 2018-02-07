# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import UserProfile


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
	class Meta:
		model = UserProfile

admin.site.register(UserProfile,UserProfileAdmin)
