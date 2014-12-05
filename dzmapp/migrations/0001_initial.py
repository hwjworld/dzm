# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='P_householder',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=2, choices=[('1', 'Male'), ('0', 'Female'), ('2', 'Other')])),
                ('street', models.CharField(max_length=100)),
                ('num', models.CharField(max_length=20)),
                ('response', models.CharField(max_length=2, choices=[('1', 'Accept'), ('0', 'Refuse')])),
                ('map_x', models.CharField(max_length=20, null=True)),
                ('map_y', models.CharField(max_length=20, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='P_Map',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('level1', models.CharField(max_length=2)),
                ('level2', models.CharField(max_length=2)),
                ('mapx', models.CharField(max_length=20)),
                ('mapy', models.CharField(max_length=20)),
                ('mappolyline', models.CharField(max_length=500, null=True)),
                ('zoom', models.IntegerField(default=17)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='P_Record',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('visit_date', models.DateTimeField()),
                ('householder', models.ForeignKey(to='dzmapp.P_householder')),
                ('map', models.ForeignKey(to='dzmapp.P_Map')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='P_Volunteer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='p_record',
            name='volunteer',
            field=models.ForeignKey(to='dzmapp.P_Volunteer'),
            preserve_default=True,
        ),
    ]
