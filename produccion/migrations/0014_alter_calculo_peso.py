# Generated by Django 5.1.3 on 2024-12-05 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0013_alter_calculo_filamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculo',
            name='peso',
            field=models.IntegerField(),
        ),
    ]
