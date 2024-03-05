# Generated by Django 4.2.10 on 2024-03-05 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rename_timespent_rep_time_spent_remove_rep_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rep',
            name='rep_date_time',
            field=models.DateTimeField(verbose_name='Date & time:'),
        ),
        migrations.AlterField(
            model_name='rep',
            name='time_spent',
            field=models.IntegerField(verbose_name='Time spent (mins):'),
        ),
    ]