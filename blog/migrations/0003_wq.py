# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-13 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190513_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='WQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=44)),
            ],
        ),
    ]
