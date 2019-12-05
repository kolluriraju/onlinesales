from django.db import models

# Create your models here.
class Admin(models.Model):
    c_no=models.IntegerField(primary_key=True)
    password=models.CharField(max_length=30)
    otp=models.IntegerField()

class Agent(models.Model):
    no=models.IntegerField()
    name=models.CharField(max_length=30)
    otp=models.IntegerField()
    agent=models.CharField(primary_key=True, max_length=30)
    password=models.CharField(max_length=30)
    image=models.ImageField(upload_to='agent/')
    address=models.CharField(max_length=50)
    c_no=models.IntegerField()

