from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    name = 'profiles'
    verbose_name = 'User Profile'

    def ready(self):
        from . import signals

