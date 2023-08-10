# Generated by Django 4.1.7 on 2023-05-16 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppBanco', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lineascredito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigo', models.PositiveSmallIntegerField(verbose_name='Codigo')),
                ('Nombre', models.TextField(max_length=30)),
                ('Montomaxino', models.PositiveBigIntegerField(verbose_name='Monto maximo')),
                ('Plazomaximo', models.PositiveSmallIntegerField(verbose_name='Plazo Maximo')),
            ],
        ),
        migrations.CreateModel(
            name='Credito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Monto', models.PositiveBigIntegerField(verbose_name='Total Credito')),
                ('Plazo', models.PositiveSmallIntegerField(choices=[('m', 6), ('m', 12), ('m', 18), ('m', 24)], default=6, verbose_name='Plazo')),
                ('Codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppBanco.lineascredito')),
                ('Documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppBanco.cliente')),
            ],
        ),
    ]