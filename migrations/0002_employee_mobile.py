# Generated by Django 3.1.2 on 2021-04-21 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotus_cooperators', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='mobile',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]