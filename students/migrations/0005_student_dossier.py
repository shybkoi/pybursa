# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extradata', '0001_initial'),
        ('students', '0004_auto_20141206_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='dossier',
            field=models.OneToOneField(null=True, blank=True, to='extradata.Dossier'),
            preserve_default=True,
        ),
    ]
