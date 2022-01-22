from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from agents.models import Agent


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Agent.objects.create(user=instance)
