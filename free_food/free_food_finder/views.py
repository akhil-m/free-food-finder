from django.shortcuts import render_to_response
from models import Event

def events(request):
    events = Event.objects.all() 
    return render_to_response('templates/events.html', {'events'=events})
