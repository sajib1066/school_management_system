from django.db import models
from academic.models import ClassRegistration, Session
from student.models import AcademicInfo

# Create your models here.

class Fees(models.Model):
    name = models.CharField(max_length=102)
    code = models.CharField(max_length=4, unique=True)
    amount = models.FloatField()
    added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name + ' fees'

class Discount(models.Model):
    name = models.CharField(max_length=102)
    code = models.CharField(max_length=4, unique=True)
    fee_type = models.ForeignKey(Fees, on_delete=models.PROTECT, blank=True)
    amount = models.IntegerField()

    def __str__(self):
        return self.name
 
class StudentFeesPaid(models.Model):
    amount = models.FloatField()
    date = models.DateField()
    student = models.ForeignKey(AcademicInfo, on_delete=models.PROTECT)
    fee_type = models.ForeignKey(Fees, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return str(self.amount) + ' paid for ' + self.student.personal_info.name 

class StudentFees(models.Model):
    student = models.ForeignKey(AcademicInfo, on_delete=models.PROTECT)
    session = models.ForeignKey(Session, on_delete=models.PROTECT)
    fees = models.ManyToManyField(Fees, blank=True)
    total_owed = models.IntegerField(default=0)
    paid = models.ManyToManyField(StudentFeesPaid, blank=True)
    total_paid = models.IntegerField(default=0)
    discount = models.ManyToManyField(Discount, blank=True)

    def __str__(self):
        return self.student.personal_info.name + ' Fees'

    def amount_due(self):
        total = 0
        paid_total=0
        for fee in self.fees.all():
            discounts = self.discount.filter(fee_type= fee)
            if discounts:
                new_fee = fee.amount
                for discount_fee in discounts:
                    new_fee = new_fee - (0.01 * fee.amount * discount_fee.amount)
                total = total + new_fee 
            else:
                total = total + fee.amount   
        for p in self.paid.all():
            paid_total = paid_total + p.amount
        return total - paid_total    

    class Meta:
        unique_together = ['student', 'session']   




