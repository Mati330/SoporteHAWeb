# Generated by Django 4.0.5 on 2022-07-15 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SoporteHAWebapp', '0006_blog'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='blog',
            new_name='blogs',
        ),
    ]