# Generated by Django 3.1 on 2022-04-18 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_remove_reason_title_second_line'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='text',
            field=models.TextField(default='Главная страница', verbose_name='Текст на главной'),
        ),
    ]
