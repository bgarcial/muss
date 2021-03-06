# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-16 12:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('muss', '0004_auto_20170914_2311'),
    ]

    operations = [
        migrations.CreateModel(
            name='HitcountTopicModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=40)),
                ('session', models.CharField(max_length=40)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topichitcount', to='muss.Topic')),
            ],
        ),
    ]
