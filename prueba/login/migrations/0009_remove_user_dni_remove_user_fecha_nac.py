# Generated by Django 4.1.7 on 2023-04-07 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_alter_user_biografia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='dni',
        ),
        migrations.RemoveField(
            model_name='user',
            name='fecha_nac',
        ),
    ]
