from django.db import models
import random

from academic.models import ClassRegistration, Session, Department
from teacher.models import PersonalInfo
from student.models import EnrolledStudent

# Create your models here.

def random_int():
    return random.randint(10000, 99999)

class SubjectRegistration(models.Model):
    select_class = models.ForeignKey(ClassRegistration, on_delete=models.CASCADE, null=True)
    subject_name = models.CharField(max_length=45)
    subject_code = models.IntegerField(unique=True, default=random_int)
    add_date = models.DateField(auto_now_add=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    periods_per_week = models.IntegerField(default=1)
    teacher =  models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.subject_name)

class Result(models.Model):
    subject = models.ForeignKey(SubjectRegistration, on_delete=models.CASCADE)
    student = models.ForeignKey(EnrolledStudent, on_delete=models.CASCADE)
    test_score = models.IntegerField()
    exam_score = models.IntegerField()
    total_score = models.IntegerField()
    add_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['subject', 'student']
    
    def __str__(self):
        return str(self.exam_score)


class StudentResult(models.Model):
    student = models.OneToOneField(EnrolledStudent, on_delete=models.CASCADE)
    result = models.ManyToManyField(Result)
    total_points = models.IntegerField(default=0)
    position = models.IntegerField(null=True, blank=True)
    approval = models.BooleanField(default=False)
    teacher_comment = models.CharField(max_length=120)
    principal_comment = models.CharField(max_length=120, null=True, blank=True)
    add_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id) 
