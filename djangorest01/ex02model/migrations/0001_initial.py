# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-26 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1024)),
                ('author', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'comment',
                'managed': True,
            },
        ),
    ]