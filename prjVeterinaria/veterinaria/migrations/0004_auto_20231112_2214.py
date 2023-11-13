# Generated by Django 3.2 on 2023-11-13 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veterinaria', '0003_auto_20231108_0726'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='localidad',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='mascota',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='provincia',
            options={'ordering': ['nombre']},
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='mascota',
        ),
        migrations.AddField(
            model_name='mascota',
            name='dueno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='veterinaria.cliente'),
        ),
    ]