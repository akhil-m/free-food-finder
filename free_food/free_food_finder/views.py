from django.shortcuts import render_to_response
from django.http import Http404, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from models import Event, UserForm

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

def register(request):
	if request.method == 'POST':
		uf = UserForm(request.POST, prefix='user')
		if uf.is_valid():
			uf.save()
			return HttpResponseRedirect('success/')
	else:
		uf = UserForm(prefix='user')
	return render_to_response('register.html', 
                                               dict(userform=uf),
                                               context_instance=RequestContext(request))

def signin(request):
	if request.method == 'POST':
	    username = request.POST['username']
	    password = request.POST['password']
	    user = authenticate(username=username, password=password)
	    if user is not None:
	        if user.is_active:
	            login(request, user)
	            return HttpResponseRedirect('/')
	    else:
	    	return render_to_response('signin.html', 
                                               dict(not_exist=True),
                                               context_instance=RequestContext(request))
	else:
		return render_to_response('signin.html', context_instance=RequestContext(request))

def success(request):
	return render_to_response('success.html')
