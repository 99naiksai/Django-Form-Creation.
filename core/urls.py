from django.urls import path
from core import views 

urlpatterns = [
    path('' , views.index),
    path('about' ,views.about),
    path('student' , views.student),
    path('employee' , views.employee),
    path('add_student',views.add_student),
    path('add_employee' , views.add_employee)
]