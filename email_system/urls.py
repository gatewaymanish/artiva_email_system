from django.urls import path
from . import views


urlpatterns = [
    path('sendemail', views.sendEmail, name='sendEmail'),
]