# Generated by Django 3.1 on 2022-04-17 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20220416_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='reason',
            name='title_second_line',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Причина. Вторая строка'),
        ),
    ]