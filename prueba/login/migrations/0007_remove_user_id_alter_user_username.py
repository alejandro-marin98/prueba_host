# Generated by Django 4.1.7 on 2023-04-04 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_alter_user_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
