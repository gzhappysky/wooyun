# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-24 12:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question',
            new_name='Bug',
        ),
    ]
