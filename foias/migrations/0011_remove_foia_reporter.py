# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 15:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foias', '0010_auto_20170222_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foia',
            name='reporter',
        ),
    ]