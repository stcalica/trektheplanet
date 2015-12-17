# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapper', '0007_blog_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='phonenumber',
            new_name='phone',
        ),
        migrations.AlterField(
            model_name='contact',
            name='location',
            field=models.ForeignKey(to='mapper.Destination'),
        ),
    ]
