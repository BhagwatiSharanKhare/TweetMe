
from django.conf.urls import url, include
from .views import (TweetListView,#, tweet_detail_view  , tweet_list_view, Tweet_Create_View
                    TweetDetailView,
                    TweetCreateView,
                    TweetUpdateView,
                    TweetDeleteView,
                    set_timezone,
                    RetweetView,
                    )
from django.views.generic.base import RedirectView


urlpatterns = [
    # url(r'^$', tweet_list_view, name='list'),
    # url(r'^1/$', tweet_detail_view, name='detail'),

    url(r'^$', RedirectView.as_view(url="/")),
    url(r'^search/$', TweetListView.as_view(), name='list'), # /tweet/
    # url(r'^(?P<pk>\d+)/$', tweet_detail_view, name='detail'),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'), # /tweet/1 keyword argument
    url(r'^create/$', TweetCreateView.as_view(), name='create'), # /tweet/create
    # url(r'^create/$', Tweet_Create_View, name='Create'),
    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'), # /tweet/1/update
    url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'), # # /tweet/1/delete
    url(r'^time/$', set_timezone, name='time'), # # /tweet/1/delete
    url(r'^(?P<pk>\d+)/retweet/$', RetweetView.as_view(), name='retweet'), # /tweet/1 keyword argument



]
