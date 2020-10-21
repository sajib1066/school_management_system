from django.urls import path

from . import views

urlpatterns = [
    path('add-period/', views.AddPeriod, name='add-period'),
    path('class-list', views.timetable_class_list, name='timetable-class-list'),
    path('generate', views.GenerateTimetable, name='generate_timetable'),
    path('view_timetable/<id>', views.ViewTimetable, name='view_timetable'),
    path('edit-timetable/<id>', views.Edit_Timetable, name='edit_timetable')
]