# Generated by Django 4.1.2 on 2022-10-06 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='i001t_tipo_forma_pago',
            fields=[
                ('co_tipo_forma_pago', models.AutoField(primary_key=True, serialize=False, verbose_name='codigo')),
                ('tx_nombre', models.CharField(help_text='Ingrese nombre de la oficina', max_length=50, verbose_name='nombre')),
                ('tx_enlace', models.SlugField(help_text='Unique value for product page URL, created from name.', max_length=110, unique=True, verbose_name='enlace')),
                ('tx_observacion', models.CharField(default='Forma de Pago', help_text='Ingrese observacion relevante del registro', max_length=50, null=True)),
                ('in_activo', models.BooleanField(default=True, verbose_name='activo')),
            ],
            options={
                'verbose_name': 'Tipo Forma de Pago',
                'verbose_name_plural': 'Tipo Formas de Pago',
                'ordering': ['-co_tipo_forma_pago'],
            },
        ),
        migrations.CreateModel(
            name='i002t_forma_pago',
            fields=[
                ('co_forma_pago', models.AutoField(primary_key=True, serialize=False, verbose_name='codigo')),
                ('tx_foto', models.ImageField(default='formapago/formapago_pratapo.jpg', upload_to='formapago', verbose_name='imagen')),
                ('in_activo', models.BooleanField(default=True, verbose_name='activo')),
                ('co_tipo', models.ForeignKey(help_text='Seleccione Tipo', on_delete=django.db.models.deletion.PROTECT, related_name='co_tipo_forma_pago_forma_pago', to='formapago.i001t_tipo_forma_pago', verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Forma de Pago',
                'verbose_name_plural': 'Formas de Pago',
                'ordering': ['-co_forma_pago'],
            },
        ),
    ]