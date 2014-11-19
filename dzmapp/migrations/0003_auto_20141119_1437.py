# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dzmapp', '0002_auto_20141119_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='p_record',
            name='map_x',
            field=models.CharField(null=True, max_length=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='p_record',
            name='map_y',
            field=models.CharField(null=True, max_length=20),
            preserve_default=True,
        ),
    ]
