# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-08 14:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0004_bug_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bugcomment',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bugcomment',
            name='description',
            field=models.TextField(max_length=256),
        ),
    ]