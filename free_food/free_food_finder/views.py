from django.shortcuts import render_to_response
from django.http import Http404
from models import Event

from datetime import datetime, timedelta

def home(request):
	return render_to_response('templates/filter.html')

def events(request, query_type):
	if query_type == 'all':
		events = Event.objects.all() 
	elif query_type == 'today':
		events = Event.objects.filter(event_date = datetime.now)
	elif query_type == 'week':
		start = datetime.now() - timedelta(days = datetime.now().weekday())
		end = start + timedelta(days = 6)
		events = Event.objects.filter(event_date__gt=start, event_date__lt=end)
	else:
		raise Http404() 
	return render_to_response('templates/events.html', {'events': events})

def event_description(request, event_id):
	try:
		event_id = int(event_id)
	except ValueError:
		raise Http404()
	event = Event.objects.get(id=event_id)
	return render_to_response('templates/event_description.html', {'event': event})