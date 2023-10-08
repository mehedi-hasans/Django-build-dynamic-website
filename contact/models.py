from django.db import models

# Create your models here.
class Contactlist(models.Model):
    address = models.TextField(max_length=800, blank=False)
    email = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.email
class Contactform(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=False)
    subject = models.CharField(max_length=100, blank=False)
    message = models.TextField(max_length=800, blank=False)

    def __str__(self):
        return self.name
    



#How to remove migrations in app
# python manage.py showmigrations
# python manage.py migrate --fake contact
# python manage.py makemigrations contact