# Generated by Django 2.2.3 on 2019-07-27 06:45

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('cinemalog', '0017_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='created_at',
            field=django_jalali.db.models.jDateField(verbose_name='Answercreatedat'),
        ),
    ]
