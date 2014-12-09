# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20141209_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zip_code', models.CharField(default=b'', max_length=15)),
                ('country', models.CharField(default=b'', max_length=255)),
                ('state', models.CharField(default=b'', max_length=255)),
                ('city', models.CharField(default=b'', max_length=255)),
                ('street', models.CharField(default=b'', max_length=255)),
                ('building', models.CharField(default=b'', max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Dossier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('favorite_color', models.CharField(default=b'red', max_length=15, choices=[(b'red', b'red'), (b'orange', b'orange'), (b'yellow', b'yellow'), (b'green', b'green'), (b'blue', b'blue'), (b'indigo', b'indigo'), (b'purple', b'purple')])),
                ('adress', models.ForeignKey(blank=True, to='extradata.Address', null=True)),
                ('unliked_courses', models.ManyToManyField(to='courses.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
