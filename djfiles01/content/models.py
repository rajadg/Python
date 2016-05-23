'''
Created on 21-May-2016

@author: dgraja
'''


from django.db import models
from django.contrib.auth.models import User


class ModelEx:
    @staticmethod
    def as_dict(entries):
        if not entries:
            raise Exception('entries must be valid list')
        filtered = lambda(entry): [pair for pair in entry.__dict__.iteritems() if pair[0][0] != '_']
        return [dict(filtered(item)) for item in entries]
    

class doc(models.Model, ModelEx):
    """
        The document table
    """
    name = models.CharField(max_length=256)
    parent = models.ForeignKey('self', blank=True, null=True,)
    size = models.IntegerField()
    blob = models.CharField(max_length=32)
    diegest = models.CharField(max_length=32)
    DOC_TYPES = (
        ('B', 'Blob'),
        ('D', 'Directory'),
        ('V', 'Version'),
    )
    type = models.CharField(max_length=1, choices=DOC_TYPES)
    owner =  models.ForeignKey(User, null=False, related_name='doc_owner')
    lastmodifier =  models.ForeignKey(User, null=False, related_name='doc_updater')
    created =  models.DateTimeField()
    updated =  models.DateTimeField()
    class Meta:
        managed = True
        db_table = "document"
        
        
class comment(models.Model):
    """
        The comments table
    """
    text = models.CharField(max_length=1024)
    class Meta:
        managed = True
        db_table = "comments"
