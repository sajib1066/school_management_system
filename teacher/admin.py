from django.contrib import admin

from . import models
# Register your models here.

admin.site.register(models.Designation)
admin.site.register(models.AddressInfo)
admin.site.register(models.EducationInfo)
admin.site.register(models.TrainingInfo)
admin.site.register(models.JobInfo)
admin.site.register(models.ExperienceInfo)
admin.site.register(models.PersonalInfo)
admin.site.register(models.GuideTeacher)
