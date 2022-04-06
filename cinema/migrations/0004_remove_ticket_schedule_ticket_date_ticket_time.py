# Generated by Django 4.0.3 on 2022-04-04 23:29

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0003_remove_ticket_theater_ticket_cinema_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='schedule',
        ),
        migrations.AddField(
            model_name='ticket',
            name='date',
            field=models.DateField(default=datetime.date(2022, 4, 4), verbose_name='data'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='horário'),
            preserve_default=False,
        ),
    ]