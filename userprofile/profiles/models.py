# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import date

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.utils.encoding import smart_unicode


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user')
    website = models.URLField(default='', blank=True)
    bio = models.TextField(default='', blank=True)
    phone = models.CharField(max_length=20, blank=True, default='')
    city = models.CharField(max_length=100, default='', blank=True)
    country = models.CharField(max_length=100, default='', blank=True)
    organization = models.CharField(max_length=100, default='', blank=True)
    def __unicode__(self):
        return smart_unicode(self.user.username)

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)



#
class Work(models.Model):
    DATE_INPUT_FORMATS = ['%m-%Y']
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    workcompleted = models.TextField(default='', blank = True)
    workplanned = models.TextField(default='', blank =True)
    approved = models.BooleanField(default = False)
    month_year = models.DateField(default=date.today)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    # user.profile.approver
    def __unicode__(self):
        return smart_unicode(self.user.username + self.month_year.date())

# def create_work(sender, **kwargs):
#     user = kwargs["instance"]
#     if kwargs[created]:
#         user_work = Work(user=user)
