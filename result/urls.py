from django.urls import path

from .views import add_subject, subject_list

urlpatterns = [
    path('add-subject', add_subject, name='add-subject'),
        path('subject-list', subject_list, name='subject-list'),
]
