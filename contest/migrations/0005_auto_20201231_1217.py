# Generated by Django 3.1.4 on 2020-12-31 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0004_auto_20201228_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='duration',
            field=models.IntegerField(blank=True),
        ),
    ]