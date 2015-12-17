# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapper', '0003_auto_20151216_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='approved',
            field=models.BooleanField(default=b'false'),
        ),
    ]
