# Create your views here.
from django.core import serializers
from django.shortcuts import render_to_response, get_object_or_404
from playlists.models import Device
import logging


logger = logging.getLogger(__name__)


def detail(request, device_id):
    device = get_object_or_404(Device, pk=device_id)
    urls = device.playlist.url_set.all()
    urlsJson = serializers.serialize("json", urls)
    return render_to_response('detail.html', {'urls': urlsJson, 'interval': device.interval})