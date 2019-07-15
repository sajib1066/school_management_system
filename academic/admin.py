from django.contrib import admin

from . import models
# Register your models here.
admin.site.register(models.Department)
admin.site.register(models.ClassInfo)
admin.site.register(models.Section)
admin.site.register(models.Session)
admin.site.register(models.Shift)
