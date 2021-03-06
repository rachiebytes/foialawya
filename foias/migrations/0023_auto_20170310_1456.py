# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-10 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foias', '0022_auto_20170308_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='foia',
            name='is_state_foia',
            field=models.BooleanField(default=False, verbose_name="Is this a FOIA filed with a state or a foreign country? (This app doesn't know about the FOIA deadlines in those places, so you won't get notifications for these, but you're welcome to track it here.)"),
        ),
        migrations.AlterField(
            model_name='foia',
            name='date_response_due_custom',
            field=models.DateField(blank=True, null=True, verbose_name='When are the records due? (Custom due date)'),
        ),
    ]
