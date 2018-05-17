# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings
import django.utils.timezone
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(unique=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, error_messages={'unique': 'A user with that username already exists.'}, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')])),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status', help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(default=True, verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups', to='auth.Group', related_name='user_set')),
                ('user_permissions', models.ManyToManyField(blank=True, related_query_name='user', help_text='Specific permissions for this user.', verbose_name='user permissions', to='auth.Permission', related_name='user_set')),
            ],
            options={
                'db_table': 'hs_user',
                'verbose_name': '用户',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('address', models.CharField(max_length=50, verbose_name='收货地址')),
                ('recieve', models.CharField(max_length=20, verbose_name='收件人')),
                ('phone_num', models.CharField(max_length=20, verbose_name='联系方式')),
                ('post_num', models.CharField(null=True, max_length=6, verbose_name='邮政编码')),
                ('user', models.ForeignKey(verbose_name='拥有者', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'hs_address',
                'verbose_name': '地址',
            },
        ),
    ]
