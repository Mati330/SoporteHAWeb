# Generated by Django 4.0.5 on 2022-07-31 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SoporteHAWebapp', '0014_alter_publicaciones_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicaciones',
            name='imagen',
        ),
        migrations.CreateModel(
            name='ImagenesPublicaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('Publicaciones', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SoporteHAWebapp.publicaciones')),
            ],
        ),
    ]