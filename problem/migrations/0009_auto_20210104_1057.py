# Generated by Django 3.1.4 on 2021-01-04 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0006_remove_contest_duration'),
        ('problem', '0008_auto_20201231_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='contest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='problems', to='contest.contest'),
        ),
    ]
