from django.db import models

# Create your models here.
class Designation(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100, unique=true)

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.name

class Upazilla(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=45, unique=true)

    def __str__(self):
        return self.name

class Union(models.Model):
    upazilla = models.ForeignKey(Upazilla, on_delete=models.CASCADE)
    name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.name

class AddressInfo(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    upazilla = models.ForeignKey(Upazilla, on_delete=models.CASCADE)
    union = models.ForeignKey(Union, on_delete=models.CASCADE)
    address = models.TextField()

    def __str__(self):
        return self.district

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
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    scale = models.IntegerField()
    grade_of_post = models.CharField(max_length=45)
    first_time_scale_due_year = models.IntegerField()
    second_time_scale_due_year = models.IntegerField()
    first_time_scale_due_year = models.IntegerField()
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
    nationality = models.CharField(max_length=45)
    religion = models.CharField(max_length=45)
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
    address = models.ForeignKey(AddressInfo, on_delete=models.CASCADE)
    education = models.ForeignKey(EducationInfo, on_delete=models.CASCADE)
    training = models.ForeignKey(TrainingInfo, on_delete=models.CASCADE)
    job = models.ForeignKey(JobInfo, on_delete=models.CASCADE)
    experience = models.ForeignKey(ExperienceInfo, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
