from django.contrib import admin
from .models import UserProfile
# from advanced_filters.admin import AdminAdvancedFiltersMixin

# admin.site.register(UserProfile)


@admin.register(UserProfile)
class ClassInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'gender')
    # advanced_filter_fields = ('name', )
    list_fields = ('user', 'gender')
