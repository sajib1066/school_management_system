from django.urls import path

from . import views

urlpatterns = [
    path('add-category', views.AddCategory, name='add-inventory-category'),
    path('delete-category', views.DeleteCategory, name='delete-inventory-category'),
    path('add-item', views.AddItem, name='add-inventory-item'),
    path('view-items', views.ViewItems, name='view-inventory-items'),
    path('view-item/<id>', views.ViewItem, name='view-inventory-item'),
    path('issue-item/', views.IssueItem, name='issue-inventory-item'),
    path('return-item/<id>', views.ReturnItem, name='return-inventory-item'),
    path('assign-item/<id>', views.AssignItem, name='assign-inventory-item'),
    path('assigned-items', views.AssignedItems, name='assigned-inventory-items'),
    path('student-assigned/<id>', views.StudentsAssigned, name='students-assigned-items')
]
