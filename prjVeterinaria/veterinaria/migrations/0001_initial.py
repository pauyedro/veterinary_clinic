# Generated by Django 3.2 on 2023-11-07 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('especie', models.CharField(max_length=50, verbose_name='Especie/Raza')),
                ('historial', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('pais', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='veterinaria.pais')),
            ],
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cp', models.CharField(max_length=10, verbose_name='Cod. Postal')),
                ('provincia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='veterinaria.provincia')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre/s')),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('nro_doc', models.IntegerField(blank=True, null=True, verbose_name='Nro de Doc.')),
                ('cuit', models.CharField(blank=True, max_length=16, null=True, verbose_name='CUIT')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('fecha_nac', models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('localidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='veterinaria.localidad')),
                ('mascota', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='veterinaria.mascota')),
                ('tipo_doc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='veterinaria.tipo_doc')),
            ],
        ),
    ]
