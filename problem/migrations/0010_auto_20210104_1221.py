# Generated by Django 3.1.4 on 2021-01-04 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0009_auto_20210104_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='problem.problem'),
        ),
    ]
