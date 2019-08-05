from django.db import models

from teacher.models import ClassRegistration

# Create your models here.

class SubjectRegistration(models.Model):
    cls = models.ForeignKey(ClassRegistration, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=45)
    subject_code = models.IntegerField(unique=True)
    marks = models.IntegerField()
    pass_mark = models.IntegerField()

    def __str__(self):
        return self.name
