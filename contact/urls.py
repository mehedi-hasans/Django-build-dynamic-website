from django.urls import path
from . import views


urlpatterns = [
    path('f', views.contact , name='contact'),
]
