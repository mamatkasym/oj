# Generated by Django 3.1.4 on 2021-01-04 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='file',
        ),
    ]
