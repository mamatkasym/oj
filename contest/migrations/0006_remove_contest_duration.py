# Generated by Django 3.1.4 on 2020-12-31 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0005_auto_20201231_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contest',
            name='duration',
        ),
    ]