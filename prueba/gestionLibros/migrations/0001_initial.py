# Generated by Django 4.1.7 on 2023-03-30 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('isbn', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30, unique=True)),
                ('paginas', models.IntegerField()),
                ('autor', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'libros',
            },
        ),
    ]