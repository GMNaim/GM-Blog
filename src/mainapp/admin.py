from django.contrib import admin
from .models import HomePageSettings, Gallery


class HomePageSettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'settings_name', 'site_name', 'active']
    list_display_links = ['id', 'settings_name']
    list_editable = ['active']


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'gallery_name',  'active']
    list_display_links = ['id', 'gallery_name']
    list_editable = ['active']


admin.site.register(HomePageSettings, HomePageSettingsAdmin)
admin.site.register(Gallery, GalleryAdmin)

