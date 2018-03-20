# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sec', '0003_blog_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='url',
            field=models.CharField(max_length=100),
        ),
    ]
