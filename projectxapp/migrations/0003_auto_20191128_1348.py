# Generated by Django 2.2.7 on 2019-11-28 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectxapp', '0002_auto_20191128_1345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proyecto',
            old_name='nombre',
            new_name='titulo',
        ),
    ]
