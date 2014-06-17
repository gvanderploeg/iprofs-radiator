from django.conf.urls import patterns, url

urlpatterns = patterns('playlists.views',
                       url(r'^$', 'index'),
                       url(r'^(?P<device_id>\d+)/$', 'detail'),
                       )