# Generated by Django 3.1 on 2022-04-07 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35, verbose_name='Область рекоммендации')),
                ('text', models.TextField(verbose_name='Рекоммендация')),
            ],
            options={
                'verbose_name': 'Рекоммендация',
                'verbose_name_plural': 'Рекоммендации',
            },
        ),
    ]
