# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-17 22:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Help_materials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.CharField(max_length=50)),
                ('professor', models.CharField(max_length=50)),
                ('discipline', models.CharField(max_length=50)),
                ('year_discipline', models.IntegerField()),
                ('upload_material', models.FileField(upload_to='')),
            ],
            options={
                'db_table': 'hmaterials',
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
