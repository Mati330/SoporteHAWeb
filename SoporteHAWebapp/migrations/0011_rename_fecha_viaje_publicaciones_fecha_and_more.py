# Generated by Django 4.0.5 on 2022-07-20 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SoporteHAWebapp', '0010_publicaciones_delete_blogs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publicaciones',
            old_name='fecha_viaje',
            new_name='fecha',
        ),
        migrations.RemoveField(
            model_name='publicaciones',
            name='pais',
        ),
    ]
