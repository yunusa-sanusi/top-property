from django.db.models.signals import post_save
from django.dispatch import receiver
from agents.models import Agent, SocialAccount


@receiver(post_save, sender=Agent)
def create_agent_social_account(sender, instance, created, **kwargs):
    if created:
        SocialAccount.objects.create(agent=instance)
