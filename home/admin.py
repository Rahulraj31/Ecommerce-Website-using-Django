from django.contrib import admin
from home.models import Contact   #added by me
# Register your models here.
admin.site.register(Contact)

#now go to apps.py copy name and in settings put in istalled apps
#terminal mai python manage.py makemigration (file banegi) then migrate (table banegi)
