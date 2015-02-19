# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='likes',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
