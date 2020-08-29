from django.contrib import admin
from home.models import Contact   #added by me
from home.models import Order   #added by me

#from home.models import  User
# Register your models here.
admin.site.register(Contact)
#admin.site.register(User)
admin.site.register(Order)


#now go to apps.py copy name and in settings put in istalled apps
#terminal mai python manage.py makemigration (file banegi) then migrate (table banegi)
