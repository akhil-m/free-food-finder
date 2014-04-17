from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'free_food_finder.views.home'),
    url(r'^filter/([A-Za-z]+)/$', 'free_food_finder.views.events'),
    url(r'^event/(\d+)/$', 'free_food_finder.views.event_description'),
    url(r'^admin/', include(admin.site.urls)),
)
