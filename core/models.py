from django.db import models
class Student(models.Model):
    sname = models.CharField(max_length=20)
    semail = models.EmailField(max_length=20)
    smno = models.IntegerField()
    def __str__(self):
        return self.sname
class Employee(models.Model):
    ename = models.CharField(max_length = 20)
    eemail = models.EmailField(max_length = 20)
    emno = models.IntegerField()
    def __str__(self):
        return self.ename
    
