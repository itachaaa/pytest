# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='bremark',
            field=models.CharField(max_length=100, default='null'),
            preserve_default=False,
        ),
    ]
