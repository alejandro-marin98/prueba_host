# Generated by Django 4.1.7 on 2023-04-05 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionLibros', '0010_alter_listas_estado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listas',
            old_name='isbn',
            new_name='book',
        ),
        migrations.RenameField(
            model_name='listas',
            old_name='username',
            new_name='user',
        ),
    ]
