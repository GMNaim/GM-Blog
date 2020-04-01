from django.db import models
from django.contrib.auth import get_user_model
import datetime
from PIL import Image

User = get_user_model()


class BaseProfile(models.Model):
    USER_TYPES = (
        (0, 'Subscriber'),
        (1, 'Blogger'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.IntegerField(null=True,
                                    choices=USER_TYPES)

    profile_picture = models.ImageField(upload_to='profile_pics/%Y/%m/%d', default='profile_pics/default_user.jpg')

    def __str__(self):
        return f'{self.user}'

    # def save(self, *args, **kwargs):
    #     """ Fixing the image in a fixed size(height and width) """
    #     super().save(*args, **kwargs)
    #
    #     img = Image.open(self.profile_picture.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)  # by thumbnail method resizing the image.
    #         img.save(self.profile_picture.path)

    class Meta:
        abstract = True


class BloggerProfile(models.Model):
    birth_date = models.DateField(null=True)

    @property
    def age(self):
        today = datetime.date.today()
        return (today.year - self.birth_date.year) - int(
            (today.month, today.day) <
            (self.birth_date.month, self.birth_date.day))

    class Meta:
        abstract = True


class SubscriberProfile(models.Model):
    class Meta:
        abstract = True


class Profile(BloggerProfile, SubscriberProfile, BaseProfile):
    pass

