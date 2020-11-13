from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Period)
admin.site.register(Timetable)
admin.site.register(Breaks)
admin.site.register(Class_Subjects)
admin.site.register(Days)
admin.site.register(SectionSubject)
admin.site.register(Teacher)