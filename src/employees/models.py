# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import smart_unicode
from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='SOME STRING')
    empid = models.CharField(max_length=120, null = True, blank=False)
    # name = models.CharField(max_length=120, null = True, blank=False)
    # email = models.EmailField(null=False, blank=False)
    # password = models.CharField(max_length=20, null = False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    division = models.CharField(max_length=120, null = False, blank=False)
    approver = models.CharField(max_length=120, null = False, blank=False)

    def __unicode__(self):
    	return smart_unicode(self.name)
# Create your models here.
