# Generated by Django 5.0.6 on 2024-07-16 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0003_remove_categoria_peliculas_pelicula_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelicula',
            name='categoria',
        ),
    ]
