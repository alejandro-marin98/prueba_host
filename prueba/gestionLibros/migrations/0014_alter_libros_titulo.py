# Generated by Django 4.1.7 on 2023-04-07 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionLibros', '0013_alter_libros_sinopsis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libros',
            name='titulo',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
