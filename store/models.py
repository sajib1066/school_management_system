from django.db import models
from account.models import Userss
from datetime import date

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=24, unique=True) 

    def __str__(self):
        return self.name 

label_choices = (
    ('null', ' '),
    ('success', 'new'),
    ('primary', 'bestseller'),
)

class Item(models.Model):
    title = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.FloatField()
    discount_price = models.FloatField(null=True, blank=True)
    photo = models.ImageField(upload_to='store-photos/', blank=True, null=True)
    description = models.CharField(max_length=65)
    label = models.CharField(max_length=17, choices=label_choices)
    currently_available = models.BooleanField(default=True)
    next_available_date = models.DateField(default=date.today, null=True)

    def __str__(self):
        return self.title  
      

class OrderItem(models.Model):
    user = models.ForeignKey(Userss, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.quantity) + ' of ' + self.item.title + ' Order Item'
        
    def get_total_item_price(self):
        return self.quantity * self.item.price 

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price 

    def amount_saved(self):
        return self.item.price - self.item.discount_price

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        else:
            return self.get_total_item_price()          

class Order(models.Model):
    user = models.ForeignKey(Userss, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + ' Order'

    def total_price(self):
        total = 0
        for item in self.items.all():
            total += item.get_final_price()
        return total        



