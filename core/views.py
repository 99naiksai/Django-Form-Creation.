from django.shortcuts import render,HttpResponse
from core.forms import Student_form,Employee_form
# Create your views here.
def index(request):
    return render(request , 'index.html')


def about(request):
    return render(request , 'about.html')


def student(request):
    context = {}
    form = Student_form(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request , 'student.html' , context)

def employee(request):
    context = {}
    form = Employee_form(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request , 'employee.html' , context)

def add_student(request):
    if request.method == 'GET':
        form = Student_form()
        return render(request , 'student.html' ,{'form':'form'})
    else:
        form = Student_form(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                pass
        return HttpResponse('datasave')

def add_employee(request):
    if request.method == 'GET':
        form = Employee_form()
        return render(request , 'employee.html' , {'form':'form'})
    else:
        form = Employee_form(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                pass
        return HttpResponse('datasave')