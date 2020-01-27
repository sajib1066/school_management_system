from django.db import models
from academic.models import ClassRegistration
from student.models import EnrolledStudent

class StudentAttendance(models.Model):
    class_name = models.ForeignKey(ClassRegistration, on_delete=models.CASCADE)
    student = models.OneToOneField(EnrolledStudent, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['student', 'date']

    def __str__(self):
        return str(self.student)
