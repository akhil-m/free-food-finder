from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'free_food_finder.views.home'),
    url(r'^filter/([A-Za-z]+)/$', 'free_food_finder.views.events'),
    url(r'^event/(\d+)/$', 'free_food_finder.views.event_description'),
    url(r'^user/register/$', 'free_food_finder.views.register'),
    url(r'^user/signin/$', 'free_food_finder.views.signin'),
    url(r'^user/register/success/$', 'free_food_finder.views.success'),
    url(r'^admin/', include(admin.site.urls)),
)
