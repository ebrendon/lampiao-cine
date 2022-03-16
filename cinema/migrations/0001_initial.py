# Generated by Django 4.0.3 on 2022-03-09 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('street', models.CharField(max_length=500)),
                ('location_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('poster', models.TextField()),
                ('description', models.TextField()),
                ('ratingAverage', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('genre', models.CharField(max_length=100)),
                ('ageGroup', models.CharField(choices=[('G', 'General Audiences'), ('PG', 'Parental Guidance Suggested'), ('PG-13', 'PG-13 – Parents Strongly Cautioned'), ('R', 'Restricted'), ('NC-17', 'Adults only')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('schedule', models.DateTimeField()),
                ('chair', models.IntegerField()),
                ('room', models.IntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.movie')),
                ('theater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.cinema')),
            ],
        ),
    ]
