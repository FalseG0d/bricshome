# Generated by Django 3.0.6 on 2020-06-22 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0016_associated_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='associated_company',
            name='width',
            field=models.IntegerField(default=0),
        ),
    ]
