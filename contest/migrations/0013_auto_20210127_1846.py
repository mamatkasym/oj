# Generated by Django 3.1.4 on 2021-01-27 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0012_auto_20210127_1724'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contestrating',
            options={'ordering': ['-penalty']},
        ),
        migrations.AddField(
            model_name='contestrating',
            name='solved_count',
            field=models.SmallIntegerField(default=0),
        ),
    ]