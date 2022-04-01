from django.urls import path
from sendsms import views

urlpatterns = [
    path('sendsms/',views.send_sms,name='sendsms'),
]