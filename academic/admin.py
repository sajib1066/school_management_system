from django.contrib import admin
from . import models


admin.site.register(models.Department)
admin.site.register(models.Section)
admin.site.register(models.Session)
admin.site.register(models.Shift)
admin.site.register(models.ClassRegistration)
admin.site.register(models.currentsession)
