# Generated by Django 5.0.6 on 2024-07-16 20:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0002_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='peliculas',
        ),
        migrations.AddField(
            model_name='pelicula',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='peliculas.categoria', verbose_name='Categoría'),
            preserve_default=False,
        ),
    ]
