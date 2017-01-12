from __future__ import unicode_literals

from django.db import models


class RSVP(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField(blank=True)
    attending = models.BooleanField()

    class Meta:
        ordering = ('last_name', 'first_name',)
        unique_together = (('first_name', 'last_name'),)
