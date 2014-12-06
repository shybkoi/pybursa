# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_coach'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='coach',
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(default=1, to='coaches.Coach'),
            preserve_default=True,
        ),
    ]
