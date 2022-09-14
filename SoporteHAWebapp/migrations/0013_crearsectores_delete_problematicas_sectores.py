# Generated by Django 4.0.5 on 2022-07-26 11:46

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SoporteHAWebapp', '0012_alter_publicaciones_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrearSectores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('fecha', models.DateField()),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'CrearSectores',
            },
        ),
        migrations.DeleteModel(
            name='Problematicas_sectores',
        ),
    ]
