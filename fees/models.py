from django.db import models
from academic.models import Session
from student.models import PersonalInfo

# Create your models here.
class Fee(models.Model):
    name = models.CharField(verbose_name='Fee name', help_text='e.g. Prep 1- 5 Tuition', max_length=120)
    amount = models.FloatField()
    session = models.ForeignKey(Session, related_name='fees', on_delete=models.CASCADE)

class StudentFee(models.Model):
    student = models.ForeignKey(PersonalInfo, on_delete=models.DO_NOTHING, related_name='fees')
    fee = models.ForeignKey(Fee, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

class StudentReceipt(models.Model):
    fee = models.ForeignKey(StudentFee, on_delete=models.PROTECT, related_name='payments')
    amount_paid = models.FloatField()
    time  = models.DateTimeField()

