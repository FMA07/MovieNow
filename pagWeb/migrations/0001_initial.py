# Generated by Django 5.1.2 on 2024-12-01 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_pelicula', models.CharField(max_length=5, unique=True)),
                ('titulo', models.CharField(max_length=30)),
                ('director', models.CharField(max_length=50)),
                ('reparto', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('disponibilidad', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Catalogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_local', models.CharField(max_length=6)),
                ('Pelicula', models.ManyToManyField(related_name='catalogos', to='pagWeb.pelicula')),
            ],
        ),
    ]
