# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0002_remove_coach_course'),
        ('courses', '0002_auto_20141206_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='coach',
            field=models.ForeignKey(default=1, to='coaches.Coach'),
            preserve_default=True,
        ),
    ]
