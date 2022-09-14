# Generated by Django 4.0.5 on 2022-07-20 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SoporteHAWebapp', '0009_alter_mda_admin_usuario_options_blogs_autor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='')),
                ('pais', models.CharField(max_length=50)),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('fecha_viaje', models.DateField()),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Publicaciones',
                'db_table': 'imageupload',
            },
        ),
        migrations.DeleteModel(
            name='blogs',
        ),
    ]
