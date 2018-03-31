
from django.conf.urls import url, include
from .views import ( UserDetailView,UserFollowView
                    )
from django.views.generic.base import RedirectView


urlpatterns = [
    # url(r'^$', tweet_list_view, name='list'),
    # url(r'^1/$', tweet_detail_view, name='detail'),

    # url(r'^$', RedirectView.as_view(url="/")),
    # url(r'^search/$', TweetListView.as_view(), name='list'), # /tweet/
    # # url(r'^(?P<pk>\d+)/$', tweet_detail_view, name='detail'),
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='detail'), # /tweet/1 keyword argument
    url(r'^(?P<username>[\w.@+-]+)/follow/$', UserFollowView.as_view(), name='follow'), # /tweet/1 keyword argument

    # url(r'^create/$', TweetCreateView.as_view(), name='create'), # /tweet/create
    # # url(r'^create/$', Tweet_Create_View, name='Create'),
    # url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'), # /tweet/1/update
    # url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'), # # /tweet/1/delete
    # url(r'^time/$', set_timezone, name='time'), # # /tweet/1/delete


]
