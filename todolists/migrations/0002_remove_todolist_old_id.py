# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-17 19:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolists', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='old_id',
        ),
    ]
