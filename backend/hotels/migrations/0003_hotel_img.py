# Generated by Django 3.1 on 2022-04-12 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_feature_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фотография'),
        ),
    ]
