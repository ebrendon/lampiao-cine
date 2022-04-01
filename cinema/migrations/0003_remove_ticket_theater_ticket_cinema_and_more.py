# Generated by Django 4.0.3 on 2022-04-01 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('cinema', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='theater',
        ),
        migrations.AddField(
            model_name='ticket',
            name='cinema',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cinema.cinema', verbose_name='cinema'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='city',
            field=models.CharField(max_length=200, verbose_name='cidade'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='location_number',
            field=models.IntegerField(verbose_name='número'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='movies',
            field=models.ManyToManyField(to='cinema.movie', verbose_name='filmes'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='name',
            field=models.CharField(max_length=200, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='street',
            field=models.CharField(max_length=500, verbose_name='rua'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='ageGroup',
            field=models.CharField(choices=[('G', 'General Audiences'), ('PG', 'Parental Guidance Suggested'), ('PG-13', 'PG-13 – Parents Strongly Cautioned'), ('R', 'Restricted'), ('NC-17', 'Adults only')], max_length=5, verbose_name='classificação indicativa'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(verbose_name='descrição'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.IntegerField(verbose_name='duração'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('Terror', 'Terror'), ('Aventura', 'Aventura'), ('Ação', 'Ação'), ('Ficção Científica', 'Ficção Científica'), ('Drama', 'Drama'), ('Comédia', 'Comédia'), ('Suspense', 'Suspense')], max_length=50, verbose_name='gênero'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.TextField(verbose_name='pôster'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='ratingAverage',
            field=models.FloatField(verbose_name='pontuação'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='título'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='chair',
            field=models.IntegerField(verbose_name='cadeira'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.movie', verbose_name='filme'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='price',
            field=models.IntegerField(verbose_name='preço'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='room',
            field=models.IntegerField(verbose_name='sala'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='schedule',
            field=models.DateTimeField(verbose_name='horário'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='usuário'),
        ),
    ]
