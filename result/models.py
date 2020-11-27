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
    add_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['subject', 'student']
    
    def __str__(self):
        return str(self.exam_score)   
        
    def total_score(self):
        return self.test_score + self.exam_score   

    def score_grade(self):
        if self.total_score() < 50:
            return 'F'
        if 50 <= self.total_score() < 55:
            return 'E'
        if 55 <= self.total_score() < 60:
            return 'D'
        if 60 <= self.total_score() < 70:
            return 'C'                        
        if 70 <= self.total_score() < 80:
            return 'B'
        if 80 <= self.total_score() < 90:
            return 'A'
        if 90 <= self.total_score() < 100:
            return 'A*'



class StudentResult(models.Model):
    student = models.OneToOneField(EnrolledStudent, on_delete=models.CASCADE)
    result = models.ManyToManyField(Result)
    position = models.IntegerField(null=True, blank=True)
    approval = models.BooleanField(default=False)
    teacher_comment = models.CharField(max_length=120)
    principal_comment = models.CharField(max_length=120, null=True, blank=True)
    add_date = models.DateField(auto_now_add=True)

    def total_points(self):
        total = 0
        for t in self.result.all():
            total += t.total_score()
        return total    

    def __str__(self):
        return str(self.id) 
