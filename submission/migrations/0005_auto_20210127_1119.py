# Generated by Django 3.1.4 on 2021-01-27 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0004_auto_20210127_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='source_code',
            field=models.TextField(default=''),
        ),
    ]