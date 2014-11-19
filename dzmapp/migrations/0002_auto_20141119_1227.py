# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dzmapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='P_Map',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('level1', models.CharField(max_length=2)),
                ('level2', models.CharField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='P_Record',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('visit_date', models.DateTimeField()),
                ('street', models.CharField(max_length=100)),
                ('num', models.CharField(max_length=20)),
                ('response', models.CharField(choices=[('A', 'Accept'), ('R', 'Refuse')], max_length=2)),
                ('map', models.ForeignKey(to='dzmapp.P_Map')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='P_Volunteer',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='record',
            name='publisher',
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
        migrations.DeleteModel(
            name='Record',
        ),
        migrations.AddField(
            model_name='p_record',
            name='volunteer',
            field=models.ForeignKey(to='dzmapp.P_Volunteer'),
            preserve_default=True,
        ),
    ]
