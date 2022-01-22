from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from autoslug import AutoSlugField


User = get_user_model()


class Agent(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user')
    address = models.CharField(max_length=100)
    age = models.IntegerField(default=18, validators=[MinValueValidator(18)])
    bio = models.TextField()
    phone_number = models.CharField(max_length=20)
    profile_picture = models.ImageField(
        upload_to='images/profile_pictures/', null=True)
    slug = AutoSlugField(
        unique=True, populate_from='user')

    @property
    def image_url(self):
        try:
            img = self.profile_picture.url
        except:
            img = ''
        return img

    def __str__(self):
        return f'Agent {self.user.username.capitalize()}'


class Social_Account(models.Model):
    class Meta:
        verbose_name_plural = 'Social Accounts'

    agent = models.ForeignKey(
        'Agent', on_delete=models.CASCADE, related_name='agent')
    url = models.URLField()

    def __str__(self):
        return f'{self.agent}'
