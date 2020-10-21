from django.db import models
from academic.models import ClassRegistration
from result.models import SubjectRegistration
from teacher.models import PersonalInfo

# Create your models here.
days = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday')
)

section_select = (
        ('Nursery', 'Nursery'),
        ('Primary', 'Primary'),
        ('Secondary', 'Secondary')
    )

class Period(models.Model):
    section = models.CharField(max_length=10, choices=section_select)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = ['section', 'start_time']

    def __str__(self):
        return str(self.start_time)


class Class_Subjects(models.Model):
    name = models.CharField(max_length=60)
    subject = models.ForeignKey(SubjectRegistration, on_delete=models.CASCADE)
    teacher = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    no_of_times_a_week = models.IntegerField()
    is_morning = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.name) 
    
class Timetable(models.Model):
    school_class = models.ForeignKey(ClassRegistration, on_delete=models.CASCADE)
    subject = models.ForeignKey(Class_Subjects, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=days)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.subject)
        
class Breaks(models.Model):
    break_choices = (
        ('Short Break', 'Short Break'),
        ('Long Break', 'Long Break'),
        ('Other', 'Other')
    ) 
    break_type = models.CharField(max_length=18, choices=break_choices)
    section = models.CharField(max_length=18, choices=section_select)
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    class Meta:
        unique_together = ['break_type', 'section']    






