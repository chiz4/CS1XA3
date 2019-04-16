# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameUser',
            fields=[
                ('u_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=64, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('register_email', models.EmailField(max_length=254, unique=True)),
                ('sex', models.CharField(max_length=32, default='male', choices=[('m', 'male'), ('f', 'famale')])),
                ('register_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'user',
                'ordering': ['register_time'],
            },
        ),
        migrations.CreateModel(
            name='ScoreRecord',
            fields=[
                ('s_id', models.AutoField(primary_key=True, serialize=False)),
                ('max_score', models.IntegerField()),
                ('get_time', models.DateTimeField(auto_now_add=True)),
                ('u_id', models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'score',
            },
        ),
    ]
