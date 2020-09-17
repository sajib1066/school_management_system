from django.db import models
from academic.models import ClassRegistration
from student.models import EnrolledStudent
from django.utils import timezone

class AttendanceManager(models.Manager):
    def create_attendance(self, std_class, std_roll, std_id, datel):
        std_cls = ClassRegistration.objects.get(name=std_class)
        std = EnrolledStudent.objects.get(roll=std_roll, class_name=std_cls)
        std_att = StudentAttendance.objects.create(
            class_name=std_cls,
            student = std,
            status = std_id,
            date = datel
        )
        return 
    def class_attendance(self, std_class, date):
        ctd = ClassRegistration.objects.get(name=std_class)
        std_att = StudentAttendance.objects.filter(class_name= ctd, date=date)   
        return std_att 

class_attendance = (
    ('Present','Present'),
    ('Absent','Absent'),
)

class StudentAttendance(models.Model):
    class_name = models.ForeignKey(ClassRegistration, on_delete=models.CASCADE)
    student = models.ForeignKey(EnrolledStudent, on_delete=models.CASCADE)
    status = models.CharField(choices=class_attendance, max_length=9)
    date = models.DateField(default=timezone.now, blank=True, null=True)

    objects = AttendanceManager()

    class Meta:
        unique_together = ['student', 'date']

    def __str__(self):
        return str(self.student.student.personal_info.name)
