# Generated by Django 3.0.6 on 2020-06-15 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_report_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/recent')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='about',
            old_name='new',
            new_name='news',
        ),
        migrations.RemoveField(
            model_name='link',
            name='icon',
        ),
        migrations.AddField(
            model_name='link',
            name='icon_in_lowercase',
            field=models.CharField(default='facebook', max_length=120),
            preserve_default=False,
        ),
    ]