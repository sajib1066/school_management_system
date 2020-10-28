from django.urls import path

from . import views

urlpatterns = [
    path('add-book/', views.AddBook, name='add-book'),
    path('add-category/', views.AddCategory, name='add-category'), 
    path('view-books/', views.ListBooks, name='view-books'),  
    path('view-book/<id>', views.ViewBook, name='view-book'),
    path('borrow-book/<id>', views.BorrowBook, name='borrow-book'),
    path('return-book/<id>', views.ReturnBook, name='return-book')
]