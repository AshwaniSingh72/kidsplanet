from django.db import models
from django.utils import timezone

# Create your models here.
class Feedback(models.Model):
    feedback_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=45)
    email=models.CharField(max_length=45)
    programe_name=models.CharField(max_length=100)
    date=models.DateField(default=timezone.now)
    feedback_text=models.TextField()
    rating=models.TextField()

class Program_detail(models.Model):
    program_name=models.CharField(max_length=100,primary_key=True)
    duration=models.CharField(max_length=20)
    fees=models.CharField(max_length=30)
    start_date=models.DateField(default=timezone.now)
    end_date=models.DateField()
    description=models.TextField()
    age_group=models.CharField(max_length=20)





class Parent_detail(models.Model):
    id=models.CharField(primary_key=True,max_length=45)
    password=models.CharField(max_length=10)
    email=models.CharField(max_length=45)
    phone=models.CharField(max_length=30)

class JobDescription(models.Model):
    job_id=models.CharField(max_length=30,primary_key=True)
    post_name=models.CharField(max_length=30)
    no_of_seat=models.IntegerField()
    last_apply=models.DateField()
    post_date=models.DateField(default=timezone.now)
    description=models.TextField()

class City_event(models.Model):
    event_id=models.IntegerField(primary_key=True)
    event_name=models.CharField(max_length=100)
    date=models.DateField()
    city=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    description=models.TextField(null=False)

class Contact(models.Model):
    name=models.CharField(max_length=45)
    email=models.CharField(max_length=45,null=False)
    phone=models.CharField(max_length=10)
    question=models.TextField()
    date=models.DateField(default=timezone.now)

Gender=[
("M","Male"),
("F","Female")
]

class AdmissionForm(models.Model):
    program_name=models.CharField(max_length=100)
    kid_name=models.CharField(max_length=30,primary_key=True)
    kid_age=models.CharField(max_length=10)
    mother_name=models.CharField(max_length=45)
    father_name=models.CharField(max_length=45)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=45)
    address=models.TextField()
    kid_gender=models.CharField(max_length=6,choices=Gender,null=False)
    school_name=models.CharField(max_length=40,null=False)
    transaction_number=models.CharField(max_length=40)

class Event(models.Model):
    event_id=models.IntegerField(primary_key=True)
    event_name=models.CharField(max_length=100)
    date=models.DateField()
    city=models.CharField(max_length=50)
    pic=models.FileField(max_length=100,upload_to="planetapp/picture",default="")
    address=models.CharField(max_length=100)
    description=models.TextField(null=False)