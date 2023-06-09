# Generated by Django 4.1.7 on 2023-04-04 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestionLibros', '0008_listas_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listas',
            name='isbn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionLibros.libros'),
        ),
        migrations.AlterField(
            model_name='listas',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
