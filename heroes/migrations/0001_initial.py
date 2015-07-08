# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Heroes',
            fields=[
                ('heroref', models.AutoField(serialize=False, primary_key=True)),
                ('id', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=50)),
                ('localized_name', models.CharField(max_length=30)),
            ],
        ),
    ]
