from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import Profile


User = get_user_model()


class UserProfileInline(admin.StackedInline):
    model = Profile


class NewUserAdmin(UserAdmin):
    inlines = [UserProfileInline]


# admin.site.unregister(User)
# admin.site.register(User, NewUserAdmin)
admin.site.register(Profile)
