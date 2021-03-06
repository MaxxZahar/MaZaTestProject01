# Generated by Django 3.1 on 2022-04-14 11:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0006_blankpage'),
        ('home', '0006_searchformmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookFormModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Адрес электронной почты')),
                ('arrival_date', models.DateField(verbose_name='День прибытия')),
                ('departure_date', models.DateField(verbose_name='День отъезда')),
                ('number_of_adults', models.IntegerField(verbose_name='Число взрослых')),
                ('number_of_children', models.IntegerField(verbose_name='Число детей')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время бронирования')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='book_hotel', to='hotels.hotel', verbose_name='Отель')),
            ],
            options={
                'verbose_name': 'Модель для формы бронирования',
                'verbose_name_plural': 'Модели для формы бронирования',
                'ordering': ('-created_at',),
            },
        ),
    ]
