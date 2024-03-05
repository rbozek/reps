# Generated by Django 4.2.10 on 2024-03-05 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rep',
            old_name='timespent',
            new_name='time_spent',
        ),
        migrations.RemoveField(
            model_name='rep',
            name='category',
        ),
        migrations.AddField(
            model_name='rep',
            name='categories',
            field=models.ManyToManyField(to='main_app.category'),
        ),
        migrations.AddField(
            model_name='rep',
            name='rep_date_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
