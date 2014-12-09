# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extradata', '0001_initial'),
        ('courses', '0008_auto_20141209_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='venue',
            field=models.ForeignKey(blank=True, to='extradata.Address', null=True),
            preserve_default=True,
        ),
    ]
