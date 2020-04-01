from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
import os
from .models import Post


@receiver(post_delete, sender=Post)
def auto_delete_image_on_delete(sender, instance, **kwargs):
    """Deletes the image from the filesystem when corresponding 'MediaFile' object is deleted"""
    if instance.thumbnail:
        if os.path.isfile(str(instance.thumbnail.path)):
            os.remove(instance.thumbnail.path)


@receiver(pre_save, sender=Post)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """Deletes old Image file from the filesystem when corresponding 'MediaFile' object is updated with new file"""

    if not instance.pk:
        print('============false=======')
        return False

    try:
        old_thumbnail = sender.objects.get(pk=instance.pk).thumbnail
        print('=====================', old_thumbnail)
    except sender.DoesNotExist:
        return False

    new_thumbnail = instance.thumbnail
    print('==============', new_thumbnail)
    if not old_thumbnail == new_thumbnail:
        print('======old is not new ========')
        if os.path.isfile(str(old_thumbnail.path)):
            print('======old is file========')
            os.remove(old_thumbnail.path)

