from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_time = models.TimeField(blank=True)
    event_date = models.DateField()
    event_description = models.TextField()
    event_location = models.CharField(max_length=50)

class UserForm(ModelForm):
    class Meta:
        model = User 
        fields = ('username', 'email', 'password')

