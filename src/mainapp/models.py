from django.db import models


class SingleActiveModel(models.Model):
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.active:
            # select all other active items
            get_settings = type(self).objects.filter(active=True)
            print('==========================================================')
            print(get_settings, type(self))
            # except self (if self already exists)
            if self.pk:
                print(self.pk)
                excluded_objects = get_settings.exclude(pk=self.pk)
                print(excluded_objects)
            # and deactivate them
            get_settings.update(active=False)
        super(SingleActiveModel, self).save(*args, **kwargs)


class HomePageSettings(SingleActiveModel):  # the active field is inherited
    site_name = models.CharField(max_length=50, default='')
    site_intro_heading = models.CharField(max_length=255, default='', blank=True)
    site_intro_text1 = models.CharField(max_length=255, default='')
    top_background_img = models.ImageField(upload_to='site_pics/%Y/%m/%d')
    site_intro_text2 = models.TextField(default='')
    middle_background_img = models.ImageField(upload_to='site_pics/%Y/%m/%d')
    middle_img_title_text = models.TextField(default='')
    newsletter_title = models.CharField(max_length=255)
    newsletter_text = models.TextField(default='')
    facebook_link = models.CharField(max_length=200, default='', blank=True)
    twitter_link = models.CharField(max_length=200, default='', blank=True)
    youtube_link = models.CharField(max_length=200, default='', blank=True)
    instagram_link = models.CharField(max_length=200, default='', blank=True)
    pinterest_link = models.CharField(max_length=200, default='', blank=True)
    site_email = models.EmailField()
    site_phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, default='', blank=True)

    settings_name = models.CharField(max_length=30, default='Settings', blank=True)

    def __str__(self):
        return f"{self.settings_name} | {self.pk}"

    class Meta:
        ordering = ['-pk']
        verbose_name = 'Home Page Setting'
        verbose_name_plural = 'Home Page Settings'


class Gallery(SingleActiveModel):  # the active field is inherited
    gallery_path = r'site_pics/gallery_pics/%Y/%m/%d'

    gallery_name = models.CharField(max_length=50, blank=True, default='Gallery Settings')
    gallery_image1 = models.ImageField(upload_to=gallery_path)
    gallery_image2 = models.ImageField(upload_to=gallery_path)
    gallery_image3 = models.ImageField(upload_to=gallery_path)
    gallery_image4 = models.ImageField(upload_to=gallery_path)

    def __str__(self):
        return f"{self.gallery_name} | {self.pk}"
    
    class Meta:
        verbose_name_plural = 'Gallery'
