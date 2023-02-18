# Generated by Django 4.1.6 on 2023-02-18 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0002_custom_populate_subscription_plans'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='subscription_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plans.subscriptionplan'),
        ),
    ]
