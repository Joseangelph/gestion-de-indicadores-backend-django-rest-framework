# Generated by Django 4.2.15 on 2024-11-28 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestion_evaluaciones', '0002_evaluacionindicador'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluacionplataforma',
            name='fecha_evaluada',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]