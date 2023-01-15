# Generated by Django 4.1.3 on 2023-01-15 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=30, verbose_name='clasificación')),
                ('clase', models.CharField(max_length=30, verbose_name='designación')),
                ('costo', models.IntegerField()),
                ('velocidad_max', models.IntegerField(verbose_name='velocidad maxima')),
            ],
            options={
                'verbose_name': 'nave',
                'verbose_name_plural': 'naves',
                'db_table': 'Nave',
            },
        ),
    ]
