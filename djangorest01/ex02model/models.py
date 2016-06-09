'''
Created on 26-May-2016

@author: dgraja
'''

from django.db import models


class comment(models.Model):
    """
        The comments table
    """
    text = models.CharField(max_length=1024)
    author = models.CharField(max_length=256)
    class Meta:
        managed = True
        db_table = "comment"

