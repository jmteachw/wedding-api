from django.conf.urls import url

from api.views import rsvp_list, rsvp_detail


urlpatterns = [
    url(r'^rsvp/$', rsvp_list),
    url(r'^rsvp/(?P<first_name>.+)/(?P<last_name>.+)$', rsvp_detail),
]
