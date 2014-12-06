# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='package',
            field=models.CharField(default=b'St', max_length=15, choices=[(b'St', b'Standart'), (b'Gl', b'Gold')]),
            preserve_default=True,
        ),
    ]
