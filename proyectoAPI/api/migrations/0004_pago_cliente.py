# Generated by Django 4.2.2 on 2023-06-11 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_prestamo_adeudo_pago'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.cliente'),
        ),
    ]