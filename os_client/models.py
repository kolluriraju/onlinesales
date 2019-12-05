from django.db import models

# Create your models here.
class Client(models.Model):
    name=models.CharField(max_length=30)
    client_uname=models.CharField(primary_key=True,max_length=30)
    password=models.CharField(max_length=30)
    photo=models.ImageField(upload_to='client/')
    c_no=models.IntegerField()
    adress=models.CharField(max_length=50)
    otp=models.IntegerField()

class Complaint(models.Model):
    client_uname=models.ForeignKey(Client,on_delete=models.CASCADE,default=None)
    comment=models.CharField(max_length=30)
    cont=models.IntegerField(default=None)