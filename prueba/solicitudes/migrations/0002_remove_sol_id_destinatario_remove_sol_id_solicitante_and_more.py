# Generated by Django 4.1.7 on 2023-04-03 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sol',
            name='id_destinatario',
        ),
        migrations.RemoveField(
            model_name='sol',
            name='id_solicitante',
        ),
        migrations.AddField(
            model_name='sol',
            name='usr_envia',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='sol',
            name='usr_recibe',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
