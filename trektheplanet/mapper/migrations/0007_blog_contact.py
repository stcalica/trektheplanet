# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mapper', '0006_destination_base'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('article', models.CharField(max_length=10000)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('date', models.DateField()),
                ('vlog', models.BooleanField(default=b'True')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('home', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('phonenumber', models.IntegerField()),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]
