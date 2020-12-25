from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Fees)
admin.site.register(Discount)
admin.site.register(StudentFees)
admin.site.register(StudentFeesPaid)
