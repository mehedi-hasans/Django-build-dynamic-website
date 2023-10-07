from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    image = models.ImageField(upload_to='about/', blank=False)
#Install Pillow for image

    def __str__(self):
        return self.title
    


    
#Class for slider
class Slider(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    image = models.ImageField(upload_to='slider/', blank=False)

    def __str__(self):
        return self.title
    
#Class for client
class Client(models.Model):
    name = models.CharField(max_length=100, blank=False)
    link = models.CharField(max_length=400, blank=False)
    image = models.ImageField(upload_to='client/', blank=False)

    def __str__(self):
        return self.name