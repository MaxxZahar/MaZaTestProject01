# Generated by Django 3.1 on 2022-04-16 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0006_blankpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='html_form_name',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Имя для HTML формы'),
        ),
    ]
