# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-13 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_forumpostupvote'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumpost',
            name='comment_number',
            field=models.IntegerField(default=0),
        ),
    ]