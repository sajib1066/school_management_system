from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=45, blank=True, null=True)
    photo = models.ImageField(upload_to='admin/', blank=True, null=True)
    gender_select = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    gender = models.CharField(choices=gender_select, max_length=6, blank=True, null=True)
    employee_select = (
        ('admin', 'Admin'),
        ('professor', 'Professor'),
        ('teacher', 'Teacher'),
        ('register', 'Register'),
        ('student', 'Student'),
    )
    employee_type = models.CharField(choices=employee_select, max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name
