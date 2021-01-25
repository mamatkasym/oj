# Generated by Django 3.1.4 on 2020-12-22 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contest', '0002_auto_20201222_1426'),
        ('problem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='problem',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='problem',
            name='contest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contest.contest'),
        ),
        migrations.AlterUniqueTogether(
            name='problem',
            unique_together={('_id', 'contest')},
        ),
    ]
