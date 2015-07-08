# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0002_auto_20150708_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='id',
            field=models.CharField(max_length=3, unique=True),
        ),
    ]
