# Generated by Django 5.1.3 on 2024-12-05 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0016_alter_calculo_costo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calculo',
            name='costo',
        ),
    ]