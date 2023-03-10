# Generated by Django 4.1.3 on 2023-01-15 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personajes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('clasificacion', models.CharField(max_length=50, verbose_name='clasificación')),
                ('designacion', models.CharField(max_length=50, verbose_name='designación')),
                ('lenguaje', models.CharField(max_length=50)),
                ('planeta_origen', models.CharField(max_length=50, verbose_name='Planeta de origen')),
                ('personajes', models.ManyToManyField(db_table='Personaje_especie', to='personajes.personaje')),
            ],
            options={
                'verbose_name': 'especie',
                'verbose_name_plural': 'especies',
                'db_table': 'Especie',
            },
        ),
    ]
