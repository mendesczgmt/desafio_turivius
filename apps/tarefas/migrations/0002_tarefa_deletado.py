# Generated by Django 5.0.7 on 2024-08-01 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='deletado',
            field=models.BooleanField(default=False),
        ),
    ]
