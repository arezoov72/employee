# Generated by Django 3.1.2 on 2021-06-15 05:38

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('lotus_cooperators', '0004_employee_birthdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='EmploymentDate',
            field=django_jalali.db.models.jDateField(null=True),
        ),
    ]