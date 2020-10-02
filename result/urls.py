from django.urls import path

from .views import add_subject, subject_list, mark_entry, mark_table, edit_subject, mark_result, my_subjects, teacher_result, student_result, students_list, student_results_list, approve_students_result, result_view_list, student_result_view, student_subject_result

urlpatterns = [
    path('add-subject', add_subject, name='add-subject'),
    path('subject-list', subject_list, name='subject-list'),
    path('subject-edit/<id>', edit_subject, name='subject-edit'),
    path('mark-entry', mark_entry, name='mark-entry'),
    path('mark-result', mark_result, name='mark-result'),
    path('mark-table/<subject>', mark_table, name='mark-table'),
    path('my-subjects', my_subjects, name='my_subjects'),
    path('teacher-result/<subject_code>', teacher_result, name='teacher_result'),
    path('student-result/<registration_no>', student_result, name='student_result'),
    path('student-list', students_list, name='result_student_list'),
    path('student-results/<registration_no>', student_results_list, name='student_results'),
    path('approve-results', approve_students_result, name='view_student_result'),
    path('student-result-list', result_view_list, name='student_result_view'),
    path('student-result-view/<id>', student_result_view, name='student_view_result'),
    path('student-subject-result/<name>/<registration_no>', student_subject_result, name='student_subject_result')
]
