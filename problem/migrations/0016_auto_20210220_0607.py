# Generated by Django 3.1.4 on 2021-02-20 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0015_auto_20210220_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editorial',
            name='ru',
            field=models.TextField(default='No editorial'),
        ),
    ]