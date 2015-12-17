# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapper', '0002_auto_20151121_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='approved',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='destination',
            name='location',
            field=models.CharField(max_length=30),
        ),
    ]
