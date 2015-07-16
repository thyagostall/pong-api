# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('player', models.IntegerField()),
                ('computer', models.IntegerField()),
                ('name', models.CharField(max_length=25)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
