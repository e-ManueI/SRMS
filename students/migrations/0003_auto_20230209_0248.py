# Generated by Django 2.2 on 2023-02-08 23:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20201207_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_date_of_birth',
            field=models.DateField(default=datetime.date(2023, 2, 9)),
        ),
    ]
