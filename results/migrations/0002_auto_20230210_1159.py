# Generated by Django 2.2 on 2023-02-10 08:59

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='declareresult',
            name='marks',
            field=jsonfield.fields.JSONField(blank=True, default=dict),
        ),
    ]
