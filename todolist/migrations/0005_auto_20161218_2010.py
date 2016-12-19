# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_auto_20161218_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.CharField(max_length=30),
        ),
    ]
