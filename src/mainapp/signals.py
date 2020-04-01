from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
import os
from .models import HomePageSettings, Gallery


@receiver(post_delete, sender=HomePageSettings)
@receiver(post_delete, sender=Gallery)
def auto_delete_image_on_delete(sender, instance, **kwargs):
    """Deletes the image from the filesystem when corresponding 'MediaFile' object is deleted"""
    """  For HomePageSettings image"""
    if sender == HomePageSettings:
        if instance.top_background_img:
            if os.path.isfile(str(instance.top_background_img.path)):
                os.remove(instance.top_background_img.path)

        if instance.middle_background_img:
            if os.path.isfile(str(instance.middle_background_img.path)):
                os.remove(instance.middle_background_img.path)

    """ For Gallery images"""
    if sender == Gallery:
        if instance.gallery_image1:
            if os.path.isfile(str(instance.gallery_image1.path)):
                os.remove(instance.gallery_image1.path)

        if instance.gallery_image2:
            if os.path.isfile(str(instance.gallery_image2.path)):
                os.remove(instance.gallery_image2.path)

        if instance.gallery_image3:
            if os.path.isfile(str(instance.gallery_image3.path)):
                os.remove(instance.gallery_image3.path)

        if instance.gallery_image4:
            if os.path.isfile(str(instance.gallery_image4.path)):
                os.remove(instance.gallery_image4.path)


@receiver(pre_save, sender=HomePageSettings)
@receiver(pre_save, sender=Gallery)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """Deletes old Image file from the filesystem when corresponding
    'MediaFile' object is updated with new file"""
    if sender == HomePageSettings:
        if not instance.pk:
            print('============false=======')
            return False

        try:
            old_top_background_img = sender.objects.get(pk=instance.pk).top_background_img
            old_middle_background_img = sender.objects.get(pk=instance.pk).middle_background_img
            print('=====================', old_top_background_img)
            print('=====================', old_middle_background_img)
        except sender.DoesNotExist:
            return False

        new_top_background_img = instance.top_background_img
        new_middle_background_img = instance.middle_background_img

        print('==============', new_top_background_img)

        if not old_top_background_img == new_top_background_img:
            print('======old is not new ========')
            if os.path.isfile(str(old_top_background_img.path)):
                print('======old is file========')
                os.remove(old_top_background_img.path)

        print('==============', new_middle_background_img)
        if not old_middle_background_img == new_middle_background_img:
            if os.path.isfile(str(old_middle_background_img.path)):
                os.remove(old_middle_background_img.path)


    """ For Gallery images"""
    if sender == Gallery:
        if not instance.pk:
            return False

        try:
            old_gallery_image1 = sender.objects.get(pk=instance.pk).gallery_image1
            old_gallery_image2 = sender.objects.get(pk=instance.pk).gallery_image2
            old_gallery_image3 = sender.objects.get(pk=instance.pk).gallery_image3
            old_gallery_image4 = sender.objects.get(pk=instance.pk).gallery_image4
        except sender.DoesNotExits:
            return False

        new_gallery_image1 = instance.gallery_image1
        new_gallery_image2 = instance.gallery_image2
        new_gallery_image3 = instance.gallery_image3
        new_gallery_image4 = instance.gallery_image4

        if not old_gallery_image1 == new_gallery_image1:
            if os.path.isfile(str(old_gallery_image1.path)):
                os.remove(old_gallery_image1.path)

        if not old_gallery_image2 == new_gallery_image2:
            if os.path.isfile(str(old_gallery_image2.path)):
                os.remove(old_gallery_image2.path)

        if not old_gallery_image3 == new_gallery_image3:
            if os.path.isfile(str(old_gallery_image3.path)):
                os.remove(old_gallery_image3.path)

        if not old_gallery_image4 == new_gallery_image4:
            if os.path.isfile(str(old_gallery_image4.path)):
                os.remove(old_gallery_image4.path)

