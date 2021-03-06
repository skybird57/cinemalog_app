# Generated by Django 2.2.3 on 2019-07-24 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('cinemalog', '0015_auto_20190724_1631'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='competition',
            options={'permissions': (('release_competition', 'Can release competiton'),), 'verbose_name': 'مسابقه', 'verbose_name_plural': 'مسابقات'},
        ),
        migrations.AlterField(
            model_name='competition',
            name='created_at',
            field=django_jalali.db.models.jDateField(verbose_name='competitioncreatedat'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
