from django.conf.urls import patterns, url

urlpatterns = patterns('playlists.views',
                       url(r'^(?P<device_id>\d+)/$', 'detail'),
                       )