# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_coach'),
        ('students', '0002_auto_20141206_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ForeignKey(default=1, to='courses.Course'),
            preserve_default=True,
        ),
    ]
