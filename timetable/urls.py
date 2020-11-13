from django.urls import path

from . import views

urlpatterns = [
    path('add-period/', views.AddPeriod, name='add-period'),
    path('add-break/', views.AddBreak, name='add-break'),
    path('add-timetable-teacher', views.AddTimetableTeacher, name='add-timetable-teacher'),
    path('delete-period/', views.DeletePeriod, name='delete-period'),
    path('delete-teacher/', views.DeleteTimetableTeacher, name='delete-timetable-teacher'),
    path('class-list', views.timetable_class_list, name='timetable-class-list'),
    path('generate', views.GenerateTimetable, name='generate_timetable'),
    path('view_timetable/<id>', views.ViewTimetable, name='view_timetable'),
    path('edit-timetable/<id>', views.Edit_Timetable, name='edit_timetable'),
    path('add-sectionsubject', views.AddSectionSubject, name='add-section-subject'),
    path('add-class-subjects', views.AddClassSubjects, name='timetable-class-subjects'),
    path('delete-class-subjects', views.DeleteClassSubjects, name='timetable-delete-class-subjects'),
    path('delete-section-subjects', views.DeleteSectionSubjects, name='timetable-delete-section-subjects'),
]