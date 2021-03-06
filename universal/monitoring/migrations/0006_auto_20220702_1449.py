# Generated by Django 3.1.5 on 2022-07-02 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0005_auto_20220702_1446'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contracts',
            new_name='Contract',
        ),
        migrations.RenameModel(
            old_name='Errors',
            new_name='Error',
        ),
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
        migrations.RenameModel(
            old_name='Manufacturers',
            new_name='System',
        ),
        migrations.AlterModelOptions(
            name='type_devices',
            options={'verbose_name': 'Тип оборудования', 'verbose_name_plural': 'Типы оборудования'},
        ),
        migrations.AlterField(
            model_name='type_devices',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Наименование типа оборудования'),
        ),
        migrations.RenameModel(
            old_name='Systems',
            new_name='Manufacturer',
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Индекс')),
                ('series', models.CharField(max_length=255, verbose_name='Серийный номер устройства')),
                ('manufacturer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring.manufacturer', verbose_name='Производитель оборудования')),
                ('type_devices_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring.type_devices', verbose_name='Тип устройства ')),
            ],
            options={
                'verbose_name': 'Устройство',
                'verbose_name_plural': 'Устройства',
            },
        ),
        migrations.AlterField(
            model_name='installed_devices',
            name='devices',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoring.device', verbose_name='Устройство'),
        ),
        migrations.DeleteModel(
            name='Devices',
        ),
    ]
