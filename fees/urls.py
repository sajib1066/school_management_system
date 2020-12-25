from django.urls import path

from . import views

urlpatterns = [
    path('add', views.AddFees, name='add-fees'),
    path('add-class-fees', views.AddClassFees, name='add-class-fees'),
    path('add-discount', views.CreateDiscount, name='create-discount'),
    path('class', views.ViewClass, name='view-class-fees'),
    path('student/<id>', views.StudentFeesView, name='student-fees'),
    path('add-fee-student/<id>', views.AddFeeStudent, name='add-fee-student'),
    path('add-paid-fee-student/<id>', views.AddPaidFeeStudent, name='add-paid-fee-student'),
    path('add-discount-fee-student/<id>', views.AddDiscountStudent, name='add-discount-student'),
    path('pdf-invoice', views.export_invoice, name='export-invoice'),
    path('paid-fee', views.PaidFee, name='paid-fee')

]