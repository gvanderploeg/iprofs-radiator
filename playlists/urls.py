from django.conf.urls import patterns, url

# Match the Device's UUID.
# Example matching URL: http://localhost:8000/radiator/67f3ec18-f709-11e3-9c79-0811968125b8/
urlpatterns = patterns('playlists.views',
                       url(r'^(?P<device_uuid>.+)/$', 'detail'),
                       )