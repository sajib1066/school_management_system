from django.db import models
from academic.models import Department
from administration.models import Designation
from address.models import District, Upazilla, Union


class AddressInfo(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    upazilla = models.ForeignKey(Upazilla, on_delete=models.CASCADE, null=True)
    union = models.ForeignKey(Union, on_delete=models.CASCADE, null=True)
    village = models.TextField()

    def __str__(self):
        return self.village

class EducationInfo(models.Model):
    name_of_exam = models.CharField(max_length=100)
    institute = models.CharField(max_length=255)
    group = models.CharField(max_length=100)
    grade = models.CharField(max_length=45)
    board = models.CharField(max_length=45)
    passing_year = models.IntegerField()

    def __str__(self):
        return self.name_of_exam

class TrainingInfo(models.Model):
    training_name = models.CharField(max_length=100)
    year = models.IntegerField()
    duration = models.IntegerField()
    place = models.CharField(max_length=100)

    def __str__(self):
        return self.training_name

class JobInfo(models.Model):
    category_choice = (
        ('bcs', 'BCS'),
        ('nationalized', 'Nationalized'),
        ('10% quota', '10% quota'),
        ('non govt.', 'Non Govt.')
    )
    category = models.CharField(choices=category_choice, max_length=45)
    joning_date = models.DateField()
    institute_name = models.CharField(max_length=100)
    job_designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    scale = models.IntegerField()
    grade_of_post = models.CharField(max_length=45)
    first_time_scale_due_year = models.IntegerField()
    second_time_scale_due_year = models.IntegerField()
    promotion_due_year = models.IntegerField()
    recreation_leave_due_year = models.IntegerField()
    expected_retirement_year = models.IntegerField()

    def __str__(self):
        return self.institute_name

class ExperienceInfo(models.Model):
    institute_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=45)
    trainer = models.CharField(max_length=45)

    def __str__(self):
        return self.institute_name

class PersonalInfo(models.Model):
    name = models.CharField(max_length=45)
    photo = models.ImageField()
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=45)
    nationality_choice = (
        ('Bangladeshi', 'Bangladeshi'),
        ('Others', 'Others')
    )
    nationality = models.CharField(max_length=45, choices=nationality_choice)
    religion_choice = (
        ('Islam', 'Islam'),
        ('Hinduism', 'Hinduism'),
        ('Buddhism', 'Buddhism'),
        ('Christianity', 'Christianity'),
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
    e_tin = models.IntegerField(unique=True)
    nid = models.IntegerField(unique=True)
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
    address = models.ForeignKey(AddressInfo, on_delete=models.CASCADE, null=True)
    education = models.ForeignKey(EducationInfo, on_delete=models.CASCADE, null=True)
    training = models.ForeignKey(TrainingInfo, on_delete=models.CASCADE, null=True)
    job = models.ForeignKey(JobInfo, on_delete=models.CASCADE, null=True)
    experience = models.ForeignKey(ExperienceInfo, on_delete=models.CASCADE, null=True)
    is_delete = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
