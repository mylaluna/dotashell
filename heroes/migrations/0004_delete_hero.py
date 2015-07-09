# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0003_auto_20150708_2224'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Hero',
        ),
    ]
