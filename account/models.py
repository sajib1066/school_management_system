from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Userss(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    is_librarian = models.BooleanField(default=False)

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    photo = models.ImageField(upload_to='admin/')
    gender_select = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    gender = models.CharField(choices=gender_select, max_length=6)
    employee_select = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('register', 'Register'),
        ('non-academic', 'non-academic'),
        ('student', 'Student'),
    )
    employee_type = models.CharField(choices=employee_select, max_length=15)

    def __str__(self):
        return self.name
