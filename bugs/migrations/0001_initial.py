# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-24 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=3000)),
                ('wooyunId', models.CharField(max_length=3000)),
                ('title', models.CharField(max_length=3000)),
                ('company', models.CharField(max_length=3000)),
                ('author', models.CharField(max_length=3000)),
                ('type', models.CharField(max_length=3000)),
                ('level', models.CharField(max_length=3000)),
                ('selfRank', models.CharField(max_length=3000)),
                ('tags', models.CharField(max_length=3000)),
            ],
        ),
    ]