# Generated by Django 4.1.6 on 2023-02-14 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_alter_picture_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.FileField(upload_to='thumbnails')),
                ('picture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thumbnails', to='images.picture')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='images.size')),
            ],
        ),
    ]
