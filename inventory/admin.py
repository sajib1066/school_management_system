from django.contrib import admin
from .models import Item, Category, Issued, ClassItems, StudentItems

# Register your models here.
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Issued)
admin.site.register(ClassItems)
admin.site.register(StudentItems)

