# Generated by Django 4.2.7 on 2025-02-21 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MiBancoVirtual', '0011_transaccion_cuentabeneficiaria_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingreso',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='ingreso',
            name='subcuenta',
        ),
        migrations.RemoveField(
            model_name='subcuenta',
            name='cuenta',
        ),
        migrations.RemoveField(
            model_name='subcuenta',
            name='perfil',
        ),
        migrations.RemoveField(
            model_name='transferencia',
            name='beneficiario',
        ),
        migrations.RemoveField(
            model_name='transferencia',
            name='ordenante',
        ),
        migrations.RemoveField(
            model_name='transaccion',
            name='beneficiario',
        ),
        migrations.RemoveField(
            model_name='transaccion',
            name='ordenante',
        ),
        migrations.RemoveField(
            model_name='transaccionprogramadadetalle',
            name='Beneficiario',
        ),
        migrations.RemoveField(
            model_name='transaccionprogramadadetalle',
            name='Ordenante',
        ),
        migrations.DeleteModel(
            name='Gasto',
        ),
        migrations.DeleteModel(
            name='Ingreso',
        ),
        migrations.DeleteModel(
            name='Subcuenta',
        ),
        migrations.DeleteModel(
            name='Transferencia',
        ),
    ]
