# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-22 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0004_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='contact',
            field=models.BigIntegerField(),
        ),
    ]
