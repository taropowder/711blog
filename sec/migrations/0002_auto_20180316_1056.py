# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sec', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='qustion_user',
            new_name='blog_user',
        ),
        migrations.AddField(
            model_name='blog',
            name='direction',
            field=models.CharField(default='1', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='url',
            field=models.CharField(max_length=50),
        ),
    ]
