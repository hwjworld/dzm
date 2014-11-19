# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dzmapp', '0003_auto_20141119_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='p_map',
            name='mapx',
            field=models.CharField(default=116.404, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='p_map',
            name='mapy',
            field=models.CharField(default=39.915, max_length=20),
            preserve_default=False,
        ),
    ]
