# Generated by Django 5.0.6 on 2024-08-26 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipo_cliente',
            field=models.CharField(choices=[('INDIVIDUAL', 'Individual'), ('CORPORATIVO', 'Corporativo'), ('ADMINISTRADOR', 'Administrador')], default='INDIVIDUAL', max_length=20),
        ),
    ]
