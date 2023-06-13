# Generated by Django 4.2.2 on 2023-06-06 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personales_exists', models.BooleanField(choices=[(True, 'S'), (False, 'N')])),
                ('crediticias_exists', models.BooleanField(choices=[(True, 'S'), (False, 'N')])),
                ('bancarias_exists', models.BooleanField(choices=[(True, 'S'), (False, 'N')])),
                ('laborales_exists', models.BooleanField(choices=[(True, 'S'), (False, 'N')])),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Porcentaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcetanje', models.FloatField(default=0)),
                ('status', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Inactivo', max_length=9)),
                ('prestamo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.prestamo')),
            ],
        ),
    ]
