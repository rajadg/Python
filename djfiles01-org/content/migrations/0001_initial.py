# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-21 14:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('size', models.IntegerField()),
                ('blob', models.CharField(max_length=32)),
                ('diegest', models.CharField(max_length=32)),
                ('type', models.CharField(choices=[(b'B', b'Blob'), (b'D', b'Directory'), (b'V', b'Version')], max_length=1)),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('lastmodifier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doc_updater', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doc_owner', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.doc')),
            ],
            options={
                'db_table': 'document',
                'managed': True,
            },
        ),
    ]
