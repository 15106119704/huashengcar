# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brande',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('name', models.CharField(max_length=10, verbose_name='品牌')),
                ('image', models.ImageField(verbose_name='汽车品牌图片', upload_to='xxx')),
                ('introduce', tinymce.models.HTMLField(blank=True, verbose_name='品牌介绍')),
            ],
            options={
                'db_table': 'hs_brande',
                'verbose_name': '汽车品牌',
            },
        ),
        migrations.CreateModel(
            name='Carstyle',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('status', models.IntegerField(choices=[(0, '售完'), (1, '在售')])),
                ('image', models.ImageField(verbose_name='车辆真实状况', upload_to='xxx')),
                ('deteil', tinymce.models.HTMLField(blank=True, verbose_name='车辆情况简介')),
                ('color', models.CharField(max_length=5, verbose_name='颜色')),
                ('price', models.DecimalField(max_digits=10, verbose_name='价格', decimal_places=2)),
                ('mileage', models.IntegerField(verbose_name='里程数')),
                ('brande', models.ForeignKey(verbose_name='品牌', to='production.Brande')),
            ],
            options={
                'db_table': 'hs_carstyle',
                'verbose_name': '车辆类型',
            },
        ),
    ]
