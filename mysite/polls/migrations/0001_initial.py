# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='station',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_station_name', models.CharField(max_length=30)),
                ('to_station_name', models.CharField(max_length=30)),
                ('station_train_code', models.CharField(max_length=10)),
                ('start_station_name', models.CharField(max_length=20)),
                ('end_station_name', models.CharField(max_length=20)),
                ('start_time', models.CharField(max_length=30)),
                ('arrive_time', models.CharField(max_length=30)),
                ('tz_num', models.CharField(max_length=10)),
                ('zy_num', models.CharField(max_length=10)),
                ('ze_num', models.CharField(max_length=10)),
                ('lishi', models.CharField(max_length=30)),
            ],
        ),
    ]
