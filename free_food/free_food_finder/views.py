from django.shortcuts import render_to_response, redirect
from django.http import Http404, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from models import Event, UserForm, Rating, Tag

from datetime import datetime, timedelta

def home(request):
	return render_to_response('templates/filter.html', context_instance=RequestContext(request))

def events(request, query_type):
	if query_type == 'all':
		events = Event.objects.filter(event_date__gt=datetime.now)
	elif query_type == 'today':
		events = Event.objects.filter(event_date = datetime.now)
	elif query_type == 'week':
		start = datetime.now() - timedelta(days = datetime.now().weekday())
		end = start + timedelta(days = 6)
		events = Event.objects.filter(event_date__gt=start, event_date__lt=end)
	else:
		raise Http404() 
	return render_to_response('templates/events.html', 
									dict(events=events), 
									context_instance=RequestContext(request))

def search(request):
	keywords = request.POST.get('query', '').split(' ')
	if len(keywords) > 0:
		events = Event.objects.filter(event_description__contains=keywords[0])
		if len(keywords) > 1:
			for keyword in keywords[1:]:
				events = events | Event.objects.filter(event_description__contains=keyword)
	return render_to_response('templates/events.html', 
									dict(events=events), 
									context_instance=RequestContext(request))

def event_description(request, event_id):
	try:
		event_id = int(event_id)
	except ValueError:
		raise Http404()

	event = Event.objects.get(id=event_id)
	tags = Tag.objects.all()
	if request.method == 'POST':
		if 'rating' in request.POST:
			rating = Rating(user=request.user, event = event, score=request.POST['rating'])
			rating.save()
		elif 'tag' in request.POST:
			for tag in tags:
				if request.POST.get(str(tag.id), False):
					print 'lol1'
					tag.event.add(event)
				else:
					print 'lol2'
					tag.event.remove(event)
				tag.save()
		else:	
			new_comment = Comment()
			new_comment.event = event
			new_comment.comment = request.POST['comment']
			new_comment.save()
			new_comment.user = request.user
			new_comment.save()

	ratings = Rating.objects.filter(event=event)
	avg_rating = 0
	if len(ratings) != 0:
		for rating in ratings:
			avg_rating += rating.score
		avg_rating /= len(ratings)
	has_rated = len(ratings.filter(user=request.user)) > 0
	star = "<i class='glyphicon glyphicon-star'></i>"
	no_star = "<i class='glyphicon glyphicon-star-empty'></i>"
	rating_html = ""
	for i in xrange(avg_rating):
		rating_html += star
	for i in xrange(5-avg_rating):
		rating_html += no_star

	tag_list = []
	for tag in tags:
		if event in tag.event.all():
			tag_list.append({'id': tag.id, 'name': tag.tag_name, 'added': True})
		else:
			tag_list.append({'id': tag.id, 'name': tag.tag_name, 'added': False})

	return render_to_response('templates/event_description.html', 
										dict(event=event, rating_html=rating_html, has_rated=has_rated, tags=tag_list), 
										context_instance=RequestContext(request))

def register(request):
	if request.method == 'POST':
		uf = UserForm(request.POST, prefix='user')
		if uf.is_valid():
			uf.save()
			return redirect('registration_success')
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

def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/')

def success(request):
	return render_to_response('success.html')
