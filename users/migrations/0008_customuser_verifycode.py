# Generated by Django 2.2.3 on 2019-08-03 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20190728_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='verifyCode',
            field=models.IntegerField(blank=True, null=True, verbose_name='UserVerifyCode'),
        ),
    ]
