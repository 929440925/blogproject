# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-21 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20171211_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='image/1.pang', upload_to='image/%Y/%m', verbose_name='主照片'),
        ),
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.ImageField(default='images/1.pang', upload_to='images/%Y/%m', verbose_name='详细照片'),
        ),
    ]