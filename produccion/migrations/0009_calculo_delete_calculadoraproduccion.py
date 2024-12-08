# Generated by Django 5.1.3 on 2024-11-30 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0008_calculadoraproduccion_delete_costocalculadora'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(max_length=100)),
                ('producto', models.CharField(max_length=100)),
                ('filamento', models.CharField(max_length=100)),
                ('peso', models.FloatField()),
                ('tiempo', models.FloatField()),
                ('costo', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='CalculadoraProduccion',
        ),
    ]
