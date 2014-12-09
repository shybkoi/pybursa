# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20141209_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='assistant',
            field=models.ForeignKey(related_name='assistant', blank=True, to='coaches.Coach', null=True),
            preserve_default=True,
        ),
    ]
