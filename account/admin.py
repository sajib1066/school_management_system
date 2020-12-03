from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Userss, UserProfile 


class UserssAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Custom Field Heading',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'is_student',
                    'is_teacher',
                ),
            },
        ),
    )



admin.site.register(Userss, UserssAdmin)
admin.site.register(UserProfile)