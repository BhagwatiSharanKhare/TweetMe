import re
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.conf import settings
from .validators import validate_content
from django.utils import timezone
from hashtags.signals import parsed_hashtags

# Create your models here.

# def validate_content(value):
#     content = value
#     if content == "abc":
#         raise ValidationError("Content Cannot be abc")
#     return value

class TweetManager(models.Manager):
    def retweet(self, user, parent_obj):
        if parent_obj.parent:
            og_parent = parent_obj.parent
        else:
            og_parent = parent_obj

        qs = self.get_queryset().filter(user=user, parent=og_parent).filter(
        updated__year=timezone.now().year,
        updated__month=timezone.now().month,
        updated__day=timezone.now().day,
        reply=False,


        )
        if qs.exists():
            return None
        obj = self.model(
            parent = parent_obj,
            user = user,
            content = parent_obj.content
        )
        obj.save()
        return obj

    def like_toggle(self, user, tweet_obj):
        if user in tweet_obj.liked.all():
            is_liked = False
            tweet_obj.liked.remove(user)
        else:
            is_liked = True
            tweet_obj.liked.add(user)
        return is_liked



# Singular # Camel Case
class Tweet(models.Model):
    parent = models.ForeignKey("self", blank=True, null=True)
    # objects     = models.Manager()
    user        = models.ForeignKey(settings.AUTH_USER_MODEL)
    liked       = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='Liked')
    reply       = models.BooleanField(verbose_name='Is a Reply?', default=False)
    content      = models.CharField(max_length=400, validators = [validate_content] )
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    objects = TweetManager()


    def __str__(self):
        return str(self.content)

    def get_absolute_url(self):
        return reverse("tweet:detail", kwargs={"pk":self.pk})

    def get_update_url(self):
        return reverse("tweet:update", kwargs={"pk":self.pk})

    def get_list_url(self):
        return reverse("tweet:list")

    def get_time_url(self):
        return reverse("tweet:time")

    def get_delete_url(self):
        return reverse("tweet:delete", kwargs={"pk":self.pk})

    def get_parent(self):
        the_parent = self

        if self.parent:
            the_parent = self.parent
        return the_parent


    def get_children(self):
        parent = self.get_parent()
        qs = Tweet.objects.filter(parent=parent)
        qs_parent = Tweet.objects.filter(pk=parent.pk)
        return (qs | qs_parent)



# model Manager

    class Meta:
        ordering = ['-updated']


    # def clean(self, *args, **kwargs):
    #     content = self.content
    #     if content == "abc":
    #         raise ValidationError("Content Cannot be abc")
    #     return super(Tweet, self).clean(*args, **kwargs)

def tweet_save_receiver(sender, instance, created, *args, **kwargs):
    if created and not instance.parent:
        # notify a user
        user_regex = r'@(?P<username>[\w.@+-]+)'
        username = re.findall(user_regex, instance.content)
        # send notification to user here

        hash_regex = r'#(?P<hashtag>[\w\d-]+)'
        hashtags = re.findall(hash_regex, instance.content)
        print(hashtags)
        parsed_hashtags.send(sender=instance.__class__, hashtag_list=hashtags)
        # send hashtag to user here


post_save.connect(tweet_save_receiver, sender=Tweet)
