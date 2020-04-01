from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from . import models


@receiver(post_save, sender=get_user_model())
def create_profile_handler(sender, instance, created, **kwargs):
    """
    Every time a user model instance is created, a corresponding user
    profile instance must be created as well. Using this function we
    will create that user profile.
    :param sender: who sending the signal. here the user model
    :param instance: the user that is newly created.
    :param created: if the user is created then true.
    :param kwargs:
    :return:
    """
    if not created:
        return
    # create the profile object, only if it is newly created.
    user_profile = models.Profile(user=instance)
    user_profile.save()
