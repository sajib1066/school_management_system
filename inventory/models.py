from django.db import models
from student.models import EnrolledStudent

# Create your models here.
class Category(models.Model):
	category=models.CharField(max_length=50)
	def __str__(self):
		return self.category		

class Item(models.Model):
    name=models.CharField(max_length=50)
    category=models.ForeignKey(Category,on_delete=models.PROTECT)
    value = models.FloatField()
    total_quantity = models.IntegerField()
    available_quantity = models.IntegerField()
    location = models.CharField(max_length=45, blank=True, null=True, help_text="Store, Admin Office")
    expiry_years = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name

    def total_value(self):
        return self.value * self.total_quantity   


class Issued(models.Model):
    individual = models.CharField(max_length=60)
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    issue_date = models.DateTimeField()
    quantity = models.IntegerField(default=1)
    return_date = models.DateTimeField()
    returned = models.BooleanField(default=False)
    comment = models.CharField(max_length=65, default='null')
    damaged = models.BooleanField(default=False)
    returned_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.individual +" took "+self.item.name


class ClassItems(models.Model):
    class_select = (
        (0, 'All'),
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
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return ' Assigned ' + self.item.name

class StudentItems(models.Model):
    classs = models.ForeignKey(ClassItems, on_delete=models.PROTECT)    
    students_given = models.ForeignKey(EnrolledStudent, on_delete=models.PROTECT)
    date_given = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.students_given.student.personal_info.name + ' ' + str(self.date_given)