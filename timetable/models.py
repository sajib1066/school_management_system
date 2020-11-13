from django.db import models
from academic.models import ClassRegistration, Section
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

class_select = (
        (1, 'Playgroup'),
        (2, 'Pre-nursery'),
        (3, 'Nursery 1'),
        (4, 'Nursery 2'),
        (5, 'Reception Year'),
        (6, 'Primary 1'),
        (7, 'Primary 2'),
        (8, 'Primary 3'),
        (9, 'Primary 4'),
        (10, 'Primary 5'),
        (11, 'JSS 1'),
        (12, 'JSS 2'),
        (13, 'JSS 3'),
        (14, 'SS 1'),
        (15, 'SS 2'),
        (16, 'SS 3')
    )

section_select = (
        ('Nursery', 'Nursery'),
        ('Lower Prep', 'Lower Prep'),
        ('Upper Prep', 'Upper Prep'),
        ('Junior Secondary', 'Junior Secondary'),
        ('Senior Secondary', 'Senior Secondary'),
    )

class Days(models.Model):
    day = models.CharField(max_length=20, choices=days) 

    def __str__(self):
        return str(self.day)  

class Teacher(models.Model):
    name = models.CharField(max_length=60)
    code = models.IntegerField()
    max_periods_a_week = models.IntegerField()
    unavailable_days = models.ManyToManyField(Days, blank=True)

    def __str__(self):
        return str(self.name) + ' ' + str(self.code)


class SectionSubject(models.Model):
    name = models.CharField(max_length=60)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='Subject_teacher')
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    additional_teacher = models.ManyToManyField(Teacher, blank=True, null=True)
    no_of_times_a_week = models.IntegerField()
    is_before_short_break = models.BooleanField(default=False)
    is_before_long_break = models.BooleanField(default=False)


    class Meta:
        unique_together = ['teacher', 'name', 'section']
    
    def __str__(self):
        return str(self.section) + ' ' + str(self.name) + ' by ' + str(self.teacher)  

class Period(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = ['section', 'start_time']

    def __str__(self):
        return str(self.start_time)


class Class_Subjects(models.Model):
    class_select = (
        (1, 'Playgroup'),
        (2, 'Pre-nursery'),
        (3, 'Nursery 1'),
        (4, 'Nursery 2'),
        (5, 'Reception Year'),
        (6, 'Primary 1'),
        (7, 'Primary 2'),
        (8, 'Primary 3'),
        (9, 'Primary 4'),
        (10, 'Primary 5'),
        (11, 'JSS 1'),
        (12, 'JSS 2'),
        (13, 'JSS 3'),
        (14, 'SS 1'),
        (15, 'SS 2'),
        (16, 'SS 3')
    )
    class_name = models.IntegerField(choices=class_select, null=True, unique=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(SectionSubject)
    
    def __str__(self):
        return str(self.class_name) 
    
class Timetable(models.Model):
    school_class = models.ForeignKey(ClassRegistration, on_delete=models.CASCADE)
    subject = models.ForeignKey(SectionSubject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=days)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.subject.name)    

class Breaks(models.Model):
    break_choices = (
        ('Short Break', 'Short Break'),
        ('Long Break', 'Long Break'),
        ('Other', 'Other')
    ) 
    break_type = models.CharField(max_length=18, choices=break_choices)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    class Meta:
        unique_together = ['break_type', 'section']    






