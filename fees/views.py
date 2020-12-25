from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
from academic.models import currentsession
from academic.forms import SelectClassForm
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.http import require_POST
from django.http import HttpResponse
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader


# Create your views here.
def AddFees(request):
    form = AddFeeForm()
    if request.method == 'POST':
        form = AddFeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fees Created Successfully')
            return redirect('add-fees')
    context = {
        'form': form
    }
    return render(request, 'fees/add-fee.html', context)


def AddClassFees(request):
    form = SelectClassForm()
    session = currentsession.objects.get()
    if request.method == 'POST':
        form = SelectClassForm(request.POST)
        if form.is_valid():
            classes = form.cleaned_data['classes']
            fee = form.cleaned_data['fee']
        students = AcademicInfo.objects.filter(class_name__in=classes)
        for student in students:
            student_fees, created = StudentFees.objects.get_or_create(student=student, session=session.current)
            if student_fees:
                student_fees.fees.add(fee)
            else:
                created.fees.add(fee) 
        messages.info(request, 'The {} fee was added for {} students'.format(fee, students.count()))
        return redirect('add-class-fees')                         
    context = {
        'form': form,
        'session': session
    }
    return render(request, 'fees/add-class-fees.html', context)

def CreateDiscount(request):
    form = AddDiscountForm()
    context = {
        'form': form,
    }    
    if request.method == 'POST':
        form = AddDiscountForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The discount has been created')
            return redirect('create-discount')
    return render(request, 'fees/add-discount.html', context)

def ViewClass(request):
    form = SelectClassForm()
    class_name = request.GET.get('select_class', None)
    if class_name:
        students = AcademicInfo.objects.filter(class_name=class_name)   
    else:
        students = None
    context = {
        'form': form,
        'students': students
    }
    return render(request, 'fees/view-class.html', context)


def StudentFeesView(request, id):
    try:
        student = StudentFees.objects.get(student__id=id)
        fee_form = StudentFeeForm()
        paid_form = StudentPaidFeeForm()
        discount_form = StudentDiscountForm()
    except ObjectDoesNotExist:
        messages.info(request, 'No Fees associated with this Student')  
        return redirect('view-class-fees')
    context = {
        'student': student,
        'fee_form': fee_form,
        'paid_form': paid_form,
        'discount_form': discount_form
    }   
    return render(request, 'fees/student-fees.html', context)

@require_POST
def AddFeeStudent(request, id):
    student = StudentFees.objects.get(id=id)
    form = StudentFeeForm(request.POST)
    if form.is_valid():
        fee = form.cleaned_data.get('fee')
        student.fees.add(fee)
        messages.info(request, 'Successfully added fee')
        return redirect('student-fees', student.student.id)
        

@require_POST
def AddPaidFeeStudent(request, id):
    student = StudentFees.objects.get(id=id)
    if request.method == 'POST':
        form = StudentPaidFeeForm(request.POST)
        if form.is_valid():
            fom = form.save(commit=False)
            fom.student = student.student
            fom.save()
            student.paid.add(fom)
            messages.success(request, 'Paid Fees successfully recorded')
            return redirect('student-fees', student.student.id)
        messages.error(request, 'Something went wrong')
        return redirect('home')    
                      
@require_POST
def AddDiscountStudent(request, id):
    student = StudentFees.objects.get(id=id)
    form = StudentDiscountForm(request.POST)
    if form.is_valid():
        fee = form.cleaned_data.get('discount')
        student.discount.add(fee)
        messages.info(request, 'Successfully added discount')
        return redirect('student-fees', student.student.id)
    messages.error(request, 'Something went wrong')
    return redirect('/')     

def PaidFee(request):
    form = StudentPaidFeeForm()
    form1 = StudentIDForm()
    reg_no = request.GET.get('reg_no', None)
    if reg_no:
        student = AcademicInfo.objects.get(registration_no=reg_no)
    else:
        student = None  
    if request.method == 'POST' and student:
        form = StudentPaidFeeForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.student = student
            form2.save()
        try:
            student_fees = StudentFees.objects.get(student=student)
            student_fees.paid.add(form2)
            messages.success(request, 'Paid Amount added successfully')
            return redirect('pay-fee')
        except ObjectDoesNotExist:
                messages.error(request, 'Can not get fees')
                return redirect('home')

    context = {
        'form': form,
        'form1': form1,
        'student': student
    }    
    return render(request, 'fees/paid-fee.html', context)

@require_POST
def export_invoice(request):
    fee_id = request.POST['id']
    student = StudentFees.objects.get(id=fee_id)
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    img = ImageReader('media\Concord-letterhead.jpg')
    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer, pagesize=A4)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.setFont("Helvetica", 19, leading=None)
    #p.drawString(200, 782, "The Concord School Invoice")
    p.setTitle(f'The Concord School Invoice For {student.student.personal_info.name}')
    #p.line(0, 780, 1000, 780)
    x1 = 320
    x2= 70
    x3 = 440
    y1 = 570
    p.setFont("Helvetica", 13, leading=None)
    fees = student.fees.all().order_by('added')
    paids = student.paid.all().order_by('date')
    discounts = student.discount.all()
    for fee in fees:
        p.drawString(x1, y1, f"{fee.amount}")
        p.drawString(x2, y1, f"{fee.added}  {fee.name}")
        y1 -= 18
    y1 -= 5    
    for paid in paids: 
        p.drawString(x3, y1, f"{paid.amount}")
        p.drawString(x2, y1, f"{paid.date} PAID FEES")                   
        y1 -= 18
    if discounts:
        y1 -= 25    
    for discount in discounts: 
        p.drawString(x3, y1, f"{discount.amount}%")
        p.drawString(x2, y1, f"{discount.name}")                   
        y1 -= 18

    #HEAders
    p.drawImage(img, 200, 710, width=150, height=120.5)
    p.drawString(70, 680, f'{student.student.guardian_info.father_name}, {student.student.guardian_info.mother_name}')
    p.drawString(70, 650, f'{student.student.personal_info.address}')
    p.drawString(400, 650, f'({student.student.personal_info.name}) ')

    # Headings
    p.setFont("Helvetica", 12, leading=None)
    p.drawCentredString(120, 610, 'PARTICULARS')    
    p.drawCentredString(340, 610, 'DEBIT')
    p.drawCentredString(460, 610, 'CREDIT')        

    # Page Border
    p.line(40,630, 550, 630)
    p.line(40,600, 550, 600)
    p.line(40, 220, 550, 220)
    p.line(40, 630, 40, 220)
    p.line(550, 630, 550, 180)
    
    #Overdue
    p.line(180, 200, 550, 200)
    p.line(180, 180, 550, 180)
    p.line(180, 180, 180, 220)
    p.drawString(190, 203, 'OVERDUE')
    p.drawString(280, 203, 'CURRENT')
    p.drawString(450, 203, 'TOTAL')

    #Overdue Values
    p.drawString(190,187, f'{student.amount_due()}') 

    #Should be paid
    p.drawString(60, 160, '***FEES ARE DUE ON THE FIRST DAY OF TERM***')
    p.line(40, 157, 550, 157)
    p.setFont("Helvetica", 13, leading=None)
    p.drawString(70, 120, 'PLEASE DETACH AND FORWARD WITH YOUR REMITTANCE TO: ')
    p.drawString(60, 100, 'The Concord School, NO 1, Olubadan Avenue, Ring-road, Ibadan')    
    p.drawString(70, 80, 'Account/Name')
    p.drawString(60,60, f'Fees Should be paid at Stanbic IBTC: 48494')
    p.drawString(70, 40, f'Account/Name: {student.student.registration_no} {student.student.guardian_info.father_name}, {student.student.guardian_info.mother_name}')
    p.drawString(370, 40, f'Amount paid ........')

    
    

    # Inner Table
    p.line(400,180,400,630)
    p.line(270,180,270,630)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f'{student.student.personal_info.name}invoice.pdf')    