# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-19 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181115_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(blank=True, max_length=250, null=True)),
                ('purchase_amount', models.CharField(blank=True, max_length=250, null=True)),
                ('user', models.CharField(blank=True, max_length=250, null=True)),
                ('reference_num', models.CharField(blank=True, max_length=250, null=True)),
                ('status', models.CharField(blank=True, max_length=250, null=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=250, null=True)),
                ('modified_date', models.DateTimeField(blank=True, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
