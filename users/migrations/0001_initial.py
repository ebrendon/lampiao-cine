# Generated by Django 4.0.3 on 2022-04-01 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=250, unique=True)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=250)),
                ('birthDate', models.DateField()),
                ('phone', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movies', models.ManyToManyField(to='cinema.movie')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
