# Generated by Django 4.2.7 on 2024-12-31 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiBancoVirtual', '0009_transaccionprogramada_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='agregarTotal',
            field=models.BooleanField(default=True),
        ),
    ]