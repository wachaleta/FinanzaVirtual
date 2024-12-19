# Generated by Django 4.2.7 on 2024-12-19 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MiBancoVirtual', '0006_alter_cuenta_saldo_real'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaccionprogramada',
            name='Abonado',
        ),
        migrations.RemoveField(
            model_name='transaccionprogramada',
            name='Beneficiario',
        ),
        migrations.RemoveField(
            model_name='transaccionprogramada',
            name='Categoria',
        ),
        migrations.RemoveField(
            model_name='transaccionprogramada',
            name='Descripcion',
        ),
        migrations.RemoveField(
            model_name='transaccionprogramada',
            name='FechaCreacion',
        ),
        migrations.RemoveField(
            model_name='transaccionprogramada',
            name='FechaLimite',
        ),
        migrations.RemoveField(
            model_name='transaccionprogramada',
            name='MetaCantidad',
        ),
        migrations.RemoveField(
            model_name='transaccionprogramada',
            name='Monto',
        ),
        migrations.RemoveField(
            model_name='transaccionprogramada',
            name='Ordenante',
        ),
        migrations.AddField(
            model_name='transaccionprogramada',
            name='Nombre',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='TransaccionProgramadaDetalle',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Descripcion', models.CharField(blank=True, max_length=300, null=True)),
                ('FechaLimite', models.DateField(null=True)),
                ('MetaCantidad', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('Abonado', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('FechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('Beneficiario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='MiBancoVirtual.Transaccion.beneficiario+', to='MiBancoVirtual.subcuenta')),
                ('Categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MiBancoVirtual.categoria')),
                ('Ordenante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='MiBancoVirtual.Transaccion.ordenante+', to='MiBancoVirtual.subcuenta')),
                ('TransaccionProgramada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MiBancoVirtual.transaccionprogramada')),
            ],
        ),
    ]