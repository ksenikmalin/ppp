# Generated by Django 3.1.5 on 2022-07-02 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0010_auto_20220702_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='system',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
    ]
