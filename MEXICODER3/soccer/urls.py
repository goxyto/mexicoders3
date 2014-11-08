from django.conf import settings
from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    url(r'^$', MainView.as_view()),
    url(r'^leagues/$', LeagueView.as_view()),
    url(r'^clubs/$', ClubView.as_view()),
    url(r'^players/$', PlayerView.as_view()),
)
