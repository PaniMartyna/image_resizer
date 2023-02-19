# Generated by Django 4.1.6 on 2023-02-18 23:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_tempurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempurl',
            name='duration',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(300), django.core.validators.MaxValueValidator(30000)]),
        ),
    ]
