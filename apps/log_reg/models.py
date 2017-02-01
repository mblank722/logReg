from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
     first_name = models.CharField(max_length=30)
     last_name = models.CharField(max_length=30)
     email = models.CharField(max_length=30)
     password = models.CharField(max_length=30)
     birth_day = models.DateField(null=True, blank=True)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

    # """docstring for ."""
    # def __init__(self, arg):
    #     super(, self).__init__()
    #     self.arg = arg
