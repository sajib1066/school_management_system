from django.urls import path

from .views import add_subject, subject_list, mark_entry, mark_table

urlpatterns = [
    path('add-subject', add_subject, name='add-subject'),
    path('subject-list', subject_list, name='subject-list'),
    path('mark-entry', mark_entry, name='mark-entry'),
    path('mark-table/<subject>', mark_table, name='mark-table'),
]
