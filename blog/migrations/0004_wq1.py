# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-13 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_wq'),
    ]

    operations = [
        migrations.CreateModel(
            name='WQ1',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=44)),
            ],
        ),
    ]
