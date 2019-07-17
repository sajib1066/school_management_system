from django.db import models

from teacher.models import ClassRegistration
# Create your models here.

class AcademicInfo(models.Model):
    class_info = models.ForeignKey(ClassRegistration, on_delete=models.CASCADE)
    roll = models.IntegerField()

    def __str__(self):
        return str(self.roll)
