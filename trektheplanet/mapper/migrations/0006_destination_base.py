# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapper', '0005_auto_20151216_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='base',
            field=models.BooleanField(default=b'false'),
        ),
    ]
