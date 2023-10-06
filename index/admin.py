from django.contrib import admin

# Register your models here.

from .models import About
admin.site.register(About) 

#python manage.py makemigrations
#python manage.py migrate