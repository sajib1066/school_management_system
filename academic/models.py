from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class ClassInfo(models.Model):
    name = models.CharField(max_length=45, unique=True)
    display_name = models.CharField(max_length=10, unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.display_name

class Section(models.Model):
    name = models.CharField(max_length=45, unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Session(models.Model):
    name = models.CharField(max_length=15, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return str(self.name)

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

class GuideTeacher(models.Model):
    name = models.OneToOneField('teacher.PersonalInfo', on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class ClassRegistration(models.Model):
    name = models.CharField(max_length=10, unique=True)
    department_select = (
        ('general', 'General'),
        ('science', 'Science'),
        ('business', 'Business'),
        ('humanities', 'Humanities')
    )
    department = models.CharField(choices=department_select, max_length=15)
    class_name = models.ForeignKey(ClassInfo, on_delete=models.CASCADE, null=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True)
    class_session = models.ForeignKey(Session,on_delete=models.CASCADE, null=True)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE, null=True)
    guide_teacher = models.OneToOneField(GuideTeacher, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['class_name', 'section', 'class_session',]

    def __str__(self):
        return self.name
