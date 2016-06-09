'''
Created on 26-May-2016

@author: dgraja
'''

from django.db import models


class contact(models.Model):
    """
        The comments table
    """
    name = models.CharField(max_length=256)
    phone = models.CharField(max_length=16)
    class Meta:
        managed = True
        db_table = "contact"

