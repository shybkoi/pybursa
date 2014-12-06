# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='package',
            field=models.CharField(default=b'Standart', max_length=15, choices=[(b'Standart', b'Standart'), (b'Gold', b'Gold')]),
            preserve_default=True,
        ),
    ]
