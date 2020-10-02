from django.contrib import admin

from .models import SubjectRegistration, Result, StudentResult

# Register your models here.
admin.site.register(SubjectRegistration)
admin.site.register(Result)
admin.site.register(StudentResult)
