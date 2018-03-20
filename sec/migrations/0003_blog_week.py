# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sec', '0002_auto_20180316_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='week',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
