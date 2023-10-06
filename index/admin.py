from django.contrib import admin

# Register your models here.

from .models import About
from .models import Slider

admin.site.register(About)
admin.site.register(Slider)


#python manage.py makemigrations
#python manage.py migrate