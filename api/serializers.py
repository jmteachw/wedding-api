from rest_framework import serializers

from api.models import RSVP


class RSVPSerializer(serializers.ModelSerializer):

    class Meta:
        model = RSVP
        fields = ('first_name', 'last_name', 'email', 'attending')
