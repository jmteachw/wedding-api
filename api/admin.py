from django.contrib import admin

from api.models import RSVP


class RSVPAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'attending')

admin.site.register(RSVP, RSVPAdmin)  # register rsvp for editing in the admin view
