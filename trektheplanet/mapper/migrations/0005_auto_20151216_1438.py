# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapper', '0004_auto_20151216_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='location',
            field=models.CharField(max_length=50),
        ),
    ]
