from django import forms
from core.models import Student , Employee
class Student_form(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
class Employee_form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'