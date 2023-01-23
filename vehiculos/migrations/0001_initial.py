# Generated by Django 4.1.3 on 2023-01-15 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=50)),
                ('clase', models.CharField(max_length=50)),
                ('costo', models.IntegerField()),
                ('velocidad_max', models.IntegerField(verbose_name='velocidad maxima')),
            ],
            options={
                'verbose_name': 'vehiculo',
                'verbose_name_plural': 'vehiculos',
                'db_table': 'Vehiculo',
            },
        ),
    ]