from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField ()
    date = models.DateField()
    #register model in admin

    def __str__(self):   # to make object name same as name of the person
        return self.name
"""
makemigrations = create changes and store in a file 
migrate = apply the pending changes created by makemigrations 
"""
