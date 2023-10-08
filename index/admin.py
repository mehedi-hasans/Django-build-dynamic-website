from django.contrib import admin

# Register your models here.

from .models import About
from .models import Slider
from .models import Client


admin.site.register(About)
admin.site.register(Slider)
admin.site.register(Client)



#python manage.py makemigrations
#python manage.py migrate