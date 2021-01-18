from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=45, unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Session(models.Model):
    session_choices = (
        ('2018/2019', '2018/2019'),
        ('2019/2020', '2019/2020'),
        ('2020/2021', '2020/2021'),
        ('2021/2022', '2021/2022'),
        ('2022/2023', '2022/2023'),
        ('2023/2024', '2023/2024'),
        ('2024/2025', '2024/2025'),
        ('2025/2026', '2025/2026'),
    )
    term_choices = (('First Term', 'First Term'),
                    ('Second Term', 'Second Term'),
                    ('Third Term', 'Third Term'),
                    )
    name = models.CharField(max_length=15, choices=session_choices)
    term = models.CharField(choices=term_choices, max_length=15)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
         unique_together = ['name', 'term']

    def __str__(self):
        return self.term +  (self.name) 

class currentsession(models.Model):
    current = models.OneToOneField(Session, on_delete=models.CASCADE, null=True)
    def save(self, *args, **kwargs):
        if not self.pk and currentsession.objects.exists():
            raise ValidationError('There can be only one currentsession')
        return super(currentsession, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.current)        

class Shift(models.Model):
    name = models.CharField(max_length=45, unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class ClassRegistration(models.Model):
    name = models.CharField(max_length=80, unique=True)
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
    class_name = models.IntegerField(choices=class_select, null=True)
    section_select = (
        ('Nursery', 'Nursery'),
        ('Lower Prep', 'Lower Prep'),
        ('Upper Prep', 'Upper Prep'),
        ('Junior Secondary', 'Junior Secondary'),
        ('Senior Secondary', 'Senior Secondary'),
    )
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    guide_teacher =  models.OneToOneField('teacher.PersonalInfo', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['class_name', 'name']

    def __str__(self):
        return self.name
