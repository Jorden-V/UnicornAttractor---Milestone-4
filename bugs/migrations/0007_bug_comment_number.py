# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-13 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0006_bugupvote'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='comment_number',
            field=models.IntegerField(default=0),
        ),
    ]