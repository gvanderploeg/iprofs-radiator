from django.contrib.auth.models import User
from django.db import models
from uuid import uuid1


class Playlist(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title


class Url(models.Model):
    playlist = models.ForeignKey(Playlist)
    url = models.CharField(max_length=255)

    def __unicode__(self):
        return self.url


class Device(models.Model):
    name = models.CharField(max_length=200)
    uuid = models.CharField(max_length=200, default=uuid1(), null=True, blank=True) # nullable and blankable to be removed, once all content adhers
    user = models.ForeignKey(User)
    playlist = models.ForeignKey(Playlist)
    interval = models.BigIntegerField('interval in ms', default=10000)

    def __unicode__(self):
        return self.name
