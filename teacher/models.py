from django.db import models
from academic.models import Department
from administration.models import Designation
from account.models import Userss

group_choices = (
    ('university', 'University'),
    ('polythenic', 'Polythenic'),
    ('college', 'College'),
)
class EducationInfo(models.Model):
    school_name = models.CharField(max_length=255)
    group = models.CharField(choices=group_choices,max_length=100)
    grade = models.CharField(max_length=45)
    nysc_information = models.CharField(max_length=45)
    graduation_year = models.IntegerField()

    def __str__(self):
        return self.school_name

class TrainingInfo(models.Model):
    training_name = models.CharField(max_length=100, null=True)
    year = models.IntegerField(null=True)
    duration = models.IntegerField(null=True)
    place = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.training_name

class JobInfo(models.Model):
    category_choice = (
        ('assistant', 'Assistant Teacher'),
        ('subject teacher', 'Subject Teacher'),
        ('class teacher', 'Class Teacher'),
        ('other', 'Others')
    )
    category = models.CharField(choices=category_choice, max_length=45)
    joining_date = models.DateField()
    job_designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.category

class ExperienceInfo(models.Model):
    former_job = models.CharField(max_length=100)
    designation = models.CharField(max_length=45)
    trainer = models.CharField(max_length=45)

    def __str__(self):
        return self.former_job

class PersonalInfo(models.Model):
    name = models.CharField(max_length=45)
    photo = models.ImageField()
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=45)
    nationality_choice = (
        ('Nigerian', 'Nigerian'),
        ('Others', 'Others')
    )
    nationality = models.CharField(max_length=45, choices=nationality_choice)
    religion_choice = (
        ('Christianity', 'Christianity'),
        ('Islam', 'Islam'),
        ('Others', 'Others')
    )
    religion = models.CharField(max_length=45, choices=religion_choice)
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    blood_group_choice = (
        ('a+', 'A+'),
        ('o+', 'O+'),
        ('b+', 'B+'),
        ('ab+', 'AB+'),
        ('a-', 'A-'),
        ('o-', 'O-'),
        ('b-', 'B-'),
        ('ab-', 'AB-')
    )
    blood_group = models.CharField(choices=blood_group_choice, max_length=5)
    driving_license_passport = models.IntegerField(unique=True)
    phone_no = models.CharField(max_length=11, unique=True)
    email = models.CharField(max_length=255, unique=True)
    father_name = models.CharField(max_length=45)
    mother_name = models.CharField(max_length=45)
    marital_status_choice = (
        ('married', 'Married'),
        ('widowed', 'Widowed'),
        ('separated', 'Separated'),
        ('divorced', 'Divorced'),
        ('single', 'Single')
    )
    marital_status = models.CharField(choices=marital_status_choice, max_length=10)
    education = models.ForeignKey(EducationInfo, on_delete=models.CASCADE, null=True)
    training = models.ForeignKey(TrainingInfo, on_delete=models.CASCADE, null=True)
    job = models.ForeignKey(JobInfo, on_delete=models.CASCADE, null=True)
    experience = models.ForeignKey(ExperienceInfo, on_delete=models.CASCADE, null=True)
    is_delete = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    login_details = models.ForeignKey(Userss, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
