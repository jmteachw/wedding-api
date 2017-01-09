from django.conf.urls import url

from api.views import add_rsvp_view


urlpatterns = [
    url(r'^add-rsvp/?$', add_rsvp_view, name='add-rsvp-view')
]
