# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 23:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='calendar',
            unique_together=set([('meal_plans', 'date', 'user')]),
        ),
    ]