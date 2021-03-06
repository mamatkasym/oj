# Generated by Django 3.1.4 on 2021-01-27 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0012_auto_20210127_1724'),
        ('problem', '0011_problem_clarification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='problem',
            old_name='_id',
            new_name='pid',
        ),
        migrations.AlterUniqueTogether(
            name='problem',
            unique_together={('pid', 'contest')},
        ),
    ]
