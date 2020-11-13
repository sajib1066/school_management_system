from django.db import models
from student.models import PersonalInfo

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category)
    isbn = models.CharField('ISBN', max_length=13, null=True, blank=True, unique=True,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    total_copies = models.IntegerField()
    available_copies = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' by ' + self.author

class Borrowed(models.Model):
    student = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateTimeField()
    return_date = models.DateTimeField()
    returned = models.BooleanField(default=False)
    returned_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.student.name+" borrowed "+self.book.title    

        

    




