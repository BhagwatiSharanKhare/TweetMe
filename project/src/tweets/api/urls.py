
from django.conf.urls import url
from .views import (
 TweetListAPIView, TweetCreateAPIView, TweetDetailAPIView, RetweetAPIView, LikeToggleAPIView)
from django.views.generic.base import RedirectView


urlpatterns = [

    #
    # url(r'^$', RedirectView.as_view(url="/")),
    url(r'^$', TweetListAPIView.as_view(), name='list'), # api/tweet/
    url(r'^(?P<pk>\d+)/retweet/$', RetweetAPIView.as_view(), name='retweet'), # /tweet/1 keyword argument
    url(r'^(?P<pk>\d+)/like/$', LikeToggleAPIView.as_view(), name='like-toggle'),
    url(r'^create/$', TweetCreateAPIView.as_view(), name='create'), # api/tweet/create
    url(r'^(?P<pk>\d+)/$', TweetDetailAPIView.as_view(), name='detail'),

    # url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'), # /tweet/1/update
    # url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'), # # /tweet/1/delete

]
