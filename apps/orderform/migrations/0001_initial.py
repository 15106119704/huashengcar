# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('order_id', models.CharField(serialize=False, primary_key=True, verbose_name='订单', max_length=50)),
                ('paystyle', models.SmallIntegerField(choices=[(0, '贷款'), (1, '支付宝'), (2, '网银')], default=1, verbose_name='支付方式')),
                ('status', models.SmallIntegerField(choices=[(0, '已下单'), (1, '已支付'), (2, '配送'), (3, '等待手续完成'), (4, '完成订单')], verbose_name='订单状态')),
                ('address', models.ForeignKey(verbose_name='收货地址', to='user.Address')),
                ('user', models.ForeignKey(verbose_name='买家', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '订单详情',
                'db_table': 'hs_order',
            },
        ),
    ]
