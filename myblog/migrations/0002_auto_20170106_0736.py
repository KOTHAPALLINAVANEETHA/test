# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='cat_name',
            new_name='catname',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='tag_name',
            new_name='tagname',
        ),
    ]
