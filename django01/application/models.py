'''
Created on 04-May-2016

@author: dgraja
'''

from django.db import models


class Contact(models.Model):
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    class Meta:
        managed = False
        db_table = "simple_contacts"
