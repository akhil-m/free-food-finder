from django.shortcuts import render_to_response
from django.http import Http404
from models import Event

def events(request):
    events = Event.objects.all() 
    return render_to_response('templates/events.html', {'events': events})

def event_description(request, event_id):
	try:
		event_id = int(event_id)
	except ValueError:
		raise Http404()
	event = Event.objects.get(id=event_id)
	return render_to_response('templates/event_description.html', {'event': event})