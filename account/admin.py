from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Userss, UserProfile 


class UserssAdmin(UserAdmin):
    pass


admin.site.register(Userss, UserssAdmin)
admin.site.register(UserProfile)