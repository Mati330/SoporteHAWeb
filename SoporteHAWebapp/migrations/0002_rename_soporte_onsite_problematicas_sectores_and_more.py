# Generated by Django 4.0.5 on 2022-06-30 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SoporteHAWebapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Soporte_onsite',
            new_name='Problematicas_sectores',
        ),
        migrations.DeleteModel(
            name='Impresoras',
        ),
        migrations.DeleteModel(
            name='Sw_de_base',
        ),
    ]
