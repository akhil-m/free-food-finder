from django.db import models

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_time = models.CharField(max_length=30)
    event_date = models.CharField(max_length=30)
    event_description = models.TextField()
    event_location = models.CharField(max_length=50)
