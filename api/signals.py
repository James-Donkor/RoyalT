# api/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, **kwargs):
    # Always ensure the profile exists
    profile, created = UserProfile.objects.get_or_create(user=instance)
    profile.save()  # Optional if you need to ensure timestamps or update hooks
