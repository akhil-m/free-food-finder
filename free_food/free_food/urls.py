from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'free_food_finder.views.home'),
    url(r'^filter/([A-Za-z]+)/$', 'free_food_finder.views.events'),
    url(r'^event/(\d+)/$', 'free_food_finder.views.event_description', name='event_detail_view'),
    url(r'^user/register/$', 'free_food_finder.views.register'),
    url(r'^user/signin/$', 'free_food_finder.views.signin'),
    url(r'^user/logout_user/$', 'free_food_finder.views.logout_user'),
    url(r'^user/register/success/$', 'free_food_finder.views.success'),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
