from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Fields
    member = models.BooleanField(default=False)  # Whether the user is member of authors

    class Meta:
        db_table = 'user'
    # Methods


class Profile(models.Model):
    # Fields
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    level = models.CharField(default='Novice',
                             max_length=100,
                             choices=[('Novice', 'Novice'),
                                      ('Amateur', 'Amateur'),
                                      ('Expert', 'Expert'),
                                      ('Master', 'Master'),
                                      ('Grand Master', 'Grand Master'),
                                      ('The Emperor', 'The Emperor')])
    image = models.ImageField(upload_to='photos/', null=True, blank=True)
    rating = models.IntegerField(default=0)
    company = models.CharField(max_length=250, null=True, blank=True)
    institute = models.CharField(max_length=250, null=True, blank=True)
    occupation = models.CharField(max_length=100, null=True, blank=True)
    language = models.CharField(max_length=100, null=True, blank=True)

    # Meta class
    class Meta:
        db_table = 'profile'
