#from __future__ import unicode_literals
from django.db import models
from datetime import datetime,date


from django.db import migrations


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField (max_length=12)

    date = models.DateTimeField()


    #register model in admin

    def __str__(self):   # to make object name same as name of the person
        return (self.name)
"""
makemigrations = create changes and store in a file 
migrate = apply the pending changes created by makemigrations 
"""
''''class User(models.Model):
    Firstname = models.CharField(max_length=122)
    Lastname = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    password=models.CharField(max_length=20)'''
    #register model in admin
class Order(models.Model):
   order_id=models.AutoField(primary_key=True)
   items_json=models.CharField(max_length=5000)
   amount=models.IntegerField(default=0)
   name=models.CharField(max_length=100)
   phone=models.CharField(max_length=12,default='')
   email=models.CharField(max_length=100)
   address=models.CharField(max_length=100,default='')
   city=models.CharField(max_length=100)
   state=models.CharField(max_length=100)
   zip_code=models.CharField(max_length=100)

   def __str__(self):
    return self.name



