# Generated by Django 4.1.7 on 2023-04-03 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0003_alter_sol_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sol',
            name='estado',
            field=models.BooleanField(auto_created=True, default='PENDIENTE'),
        ),
    ]
