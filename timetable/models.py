from django.db import models
from academic.models import ClassRegistration
from result.models import SubjectRegistration

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
    day = models.CharField(max_length=10, choices=days)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = ['section', 'day', 'start_time']

    def __str__(self):
        return self.day + ' ' + str(self.start_time)


class Timetable(models.Model):
    school_class = models.ForeignKey(ClassRegistration, on_delete=models.CASCADE)
    subject = models.ForeignKey(SubjectRegistration, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)

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






