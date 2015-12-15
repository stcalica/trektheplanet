# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import django_countries.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mapper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='visited',
            field=models.BooleanField(default=datetime.datetime(2015, 11, 21, 22, 15, 34, 322906, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='destination',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
