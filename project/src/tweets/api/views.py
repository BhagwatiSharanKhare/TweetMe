from rest_framework import generics
from django.db.models import Q
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response


from tweets.models import Tweet

from .pagination import StandardResultsPagination
from .serializers import TweetModelSerializer

class LikeToggleAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk, format=None):
        tweet_qs = Tweet.objects.filter(pk=pk)
        message = "Not allowed"
        if request.user.is_authenticated():
            is_liked=Tweet.objects.like_toggle(request.user, tweet_qs.first())
            return Response({'liked': is_liked})
        return Response({"message": message}, status=400)

class RetweetAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk, format=None):
        tweet_qs = Tweet.objects.filter(pk=pk)
        # print(tweet_qs)
        message = "Not allowed"
        if tweet_qs.exists() and tweet_qs.count() == 1:
            # if request.user.is_authenticated():
            new_tweet=Tweet.objects.retweet(request.user, tweet_qs.first())
            # print("abc")
            # print(new_tweet)
            if new_tweet is not None:
                data = TweetModelSerializer(new_tweet).data
                return Response(data)
            message = "Cannot retweet the same in 1 day"
        return Response({"message": message}, status=400)

class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class = TweetModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TweetDetailAPIView(generics.ListAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetModelSerializer
    pagination_class = StandardResultsPagination
    permission_classes = [permissions.AllowAny]

    def get_queryset(self, *args, **kwargs):
        tweet_id = self.kwargs.get("pk")
        qs = Tweet.objects.filter(pk=tweet_id)
        if qs.exists() and qs.count() == 1:
            parent_obj = qs.first()
            qs1 = parent_obj.get_children()
            qs = (qs | qs1).distinct().extra(select={"parent_id_null": 'parent_id is NULL'})
        return qs.order_by("-parent_id_null", "updated")




class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer
    pagination_class = StandardResultsPagination

    def get_serializer_context(self, *args, **kwargs):
        context = super(TweetListAPIView, self).get_serializer_context(*args, **kwargs)
        context['request'] = self.request
        # print(context)
        return context


    def get_queryset(self, *args, **kwargs):
        requested_user = self.kwargs.get("username")
        if requested_user:
            # they_follow = self.request.user.profile.get_following()
            # qs1 = Tweet.objects.filter(user__in=im_following)
            qs = Tweet.objects.filter(user__username=requested_user).order_by('-updated')
            # qs = (qs1 | qs2).distinct()
        else:
            im_following = self.request.user.profile.get_following()
            qs1 = Tweet.objects.filter(user__in=im_following)
            qs2 = Tweet.objects.filter(user=self.request.user)
            qs = (qs1 | qs2).distinct().order_by('-updated')

        # print(self.request.GET)
        query = self.request.GET.get('q', None)

        # print(query)
        if query is not None:
            qs = qs.filter(
            Q(content__icontains=query) |
            Q(user__username__icontains=query)
            )
        # print(qs)
        return qs

class SearchTweetAPIView(generics.ListAPIView):
    queryset = Tweet.objects.all().order_by("updated")
    serializer_class = TweetModelSerializer
    pagination_class = StandardResultsPagination

    def get_serializer_context(self, *args, **kwargs):
        context = super(SearchTweetAPIView, self).get_serializer_context(*args, **kwargs)
        context['request'] = self.request
        # print(context)
        return context

    def get_queryset(self, *args, **kwargs):
        qs = self.queryset
        # print(self.request.GET)
        query = self.request.GET.get('q', None)

        # print(query)
        if query is not None:
            qs = qs.filter(
            Q(content__icontains=query) |
            Q(user__username__icontains=query)
            )
        # print(qs)
        return qs
