# Generated by Django 4.1.7 on 2023-04-05 15:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('solicitudes', '0006_alter_sol_usr_envia_alter_sol_usr_recibe'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='sol',
            new_name='Solicitudes',
        ),
    ]
