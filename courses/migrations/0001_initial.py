# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('technology', models.CharField(default=b'Python', max_length=15, choices=[(b'Python', b'Python/Django'), (b'JS', b'JavaScript'), (b'Ruby', b'Ruby on rails')])),
                ('name', models.CharField(max_length=255)),
                ('desription', models.CharField(max_length=255)),
                ('teacher', models.CharField(max_length=255)),
                ('assistant', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('finish_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
