from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(AcademicInfo)
admin.site.register(PersonalInfo)
admin.site.register(StudentAddressInfo)
admin.site.register(GuardianInfo)
admin.site.register(EmergencyContactDetails)
admin.site.register(PreviousAcademicInfo)
admin.site.register(PreviousAcademicCertificate)
admin.site.register(EnrolledStudent)
