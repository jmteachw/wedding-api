from rest_framework import serializers

from api.models import RSVP


class RSVPSerializer(serializers.Serializer):

    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    attending = serializers.BooleanField(required=True)

    def create(self, validated_data):
        """
        Create and return a new `RSVP` instance, given the validated data.
        """
        return RSVP.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `RSVP` instance, given the validated data.
        """
        instance.email = validated_data.get('email', instance.email)
        instance.attending = validated_data.get('attending', instance.attending)
        instance.save()
        return instance
