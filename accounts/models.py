from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'


class Agent(models.Model):
    user = models.OneToOneField(
        'User', on_delete=models.CASCADE, related_name='user')
    address = models.CharField(max_length=100)
    age = models.IntegerField(default=18, validators=[MinValueValidator(18)])
    bio = models.TextField()
    phone_number = models.CharField(max_length=20)
    profile_picture = models.ImageField(
        upload_to='images/profile_pictures/', null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'Agent {self.username}'


class Social_Account(models.Model):
    class Meta:
        verbose_name_plural = 'Social Accounts'

    agent = models.ForeignKey(
        'Agent', on_delete=models.CASCADE, related_name='agent')
    url = models.URLField()

    def __str__(self):
        return f'{self.agent}'
