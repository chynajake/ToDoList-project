# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todolist', '0002_auto_20161202_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('task', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('date', models.CharField(max_length=100)),
                ('executor', models.EmailField(max_length=254)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='author',
        ),
        migrations.DeleteModel(
            name='Tasks',
        ),
    ]
