# Generated by Django 4.2.15 on 2024-10-12 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestion_indicadores', '0002_categoriaanalisis_concepto_componente_concepto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indicador',
            name='categoria_analisis',
        ),
        migrations.RemoveField(
            model_name='indicador',
            name='componente',
        ),
        migrations.RemoveField(
            model_name='indicador',
            name='destino_impacto',
        ),
    ]
