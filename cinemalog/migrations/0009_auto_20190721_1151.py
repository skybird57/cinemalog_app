# Generated by Django 2.2.3 on 2019-07-21 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinemalog', '0008_auto_20190721_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationversion',
            name='platform',
            field=models.IntegerField(choices=[(1, 'Android'), (2, 'IOS')], verbose_name='نوع سیستم'),
        ),
    ]
