# Generated by Django 3.1.4 on 2021-02-01 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210201_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='photos/default.png', upload_to='photos/'),
        ),
    ]
