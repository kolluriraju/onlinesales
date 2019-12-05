from django.db import models
from os_admin.models import Agent
from os_client.models import Client

# Create your models here.
class Property(models.Model):
    p_no = models.AutoField(primary_key=True)
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    location=models.CharField(max_length=30)
    photo=models.ImageField(upload_to='Property/')
    size=models.CharField(max_length=20)
    price=models.CharField(max_length=30)
    facing=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    comment=models.CharField(max_length=30)
    add_date=models.DateField(auto_now_add=True)
    sold_date=models.DateField(auto_now_add=True)

class Soldproperty(models.Model):
    p_no=models.ForeignKey(Property,on_delete=models.CASCADE)
    date_of_sold=models.DateField(auto_now_add=True)
    client_uname = models.ForeignKey(Client,on_delete=models.CASCADE,default=None)


class PropertyBlocked(models.Model):
    bno=models.AutoField(primary_key=True)
    p_no=models.ForeignKey(Property,on_delete=models.CASCADE)
    client_uname=models.ForeignKey(Client,on_delete=models.CASCADE)


