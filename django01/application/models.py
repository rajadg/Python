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
        managed = True
        db_table = "simple_contacts"

class Location(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    name = models.CharField(max_length=16)
    latitude = models.CharField(max_length=16)
    longitude = models.CharField(max_length=16)
    class Meta:
        managed = True
        db_table = "location"
