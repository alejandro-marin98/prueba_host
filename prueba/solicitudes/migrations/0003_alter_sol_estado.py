# Generated by Django 4.1.7 on 2023-04-03 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0002_remove_sol_id_destinatario_remove_sol_id_solicitante_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sol',
            name='estado',
            field=models.IntegerField(choices=[(0, 'PENDIENTE'), (1, 'ACEPTADA'), (2, 'DENEGADA')], default=0),
        ),
    ]