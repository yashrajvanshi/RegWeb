from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(null=True,blank=True,max_length=100)
    address = models.CharField(null=True,blank=True,max_length=255)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=100)
    subject = models.ManyToManyField('Subject',through="Mark",
                                     through_fields=('student_id', 'subject_id'),)
    
    
    
    def __str__(self):
        return f'{self.student_id} Profile'
    
    
class Subject(models.Model):
    
    subject_name = models.CharField(unique=True,max_length=100)
    
    def __str__(self):
        return f'{self.subject_name}'
    
class Mark(models.Model):
    
    class Meta:
        unique_together = (('student_id', 'subject_id'),)
    
    student_id = models.ForeignKey('Student',on_delete=models.CASCADE)
    subject_id = models.ForeignKey('Subject',on_delete=models.CASCADE)
    marks = models.IntegerField()
    
    
    def __str__(self):
        return f'{self.marks}'
    
    
