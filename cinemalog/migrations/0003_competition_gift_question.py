# Generated by Django 2.2.3 on 2019-07-13 10:20

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('cinemalog', '0002_applicationversion_news_sendadv_sendpush'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='competitiontitle')),
                ('create_at', django_jalali.db.models.jDateField(verbose_name='competitioncreatedate')),
            ],
            options={
                'verbose_name': 'Competition',
                'verbose_name_plural': 'Competitions',
            },
        ),
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='gifttitle')),
                ('desc', models.TextField(max_length=200, verbose_name='giftdesc')),
                ('pic', models.FileField(null=True, upload_to='', verbose_name='giftpic')),
                ('deliverDate', django_jalali.db.models.jDateField(verbose_name='giftdeliverdate')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=100, verbose_name='questionuestion')),
                ('answer1', models.CharField(max_length=30, verbose_name='questionanswer1')),
                ('answer2', models.CharField(max_length=30, verbose_name='questionanswer2')),
                ('answer3', models.CharField(max_length=30, verbose_name='questionanswer3')),
                ('answer4', models.CharField(max_length=30, verbose_name='questionanswer4')),
                ('correct_answer', models.CharField(max_length=30, verbose_name='questioncorrect')),
                ('score_ca', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='questionscore_ca')),
                ('score_wa', models.IntegerField(choices=[(-1, -1), (-2, -2), (-3, -3), (-4, -4), (-5, -5)], null=True, verbose_name='questionscore_wa')),
                ('Competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemalog.Competition')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
    ]