from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django import forms
from django.forms.utils import ErrorList
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .forms import TweetModelForm
from .models import Tweet
from .mixins import FormUserNeededMixin, UserOwnerMixin
from django.shortcuts import redirect, render
import pytz
# Create your views here.

# create retreive update delete list/search

# Create

class RetweetView(View):
    def get(self, request, pk, *args, **kwargs):
        tweet = get_object_or_404(Tweet, pk=pk)
        if request.user.is_authenticated():
            new_tweet=Tweet.objects.retweet(request.user, tweet)
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect(tweet.get_absolute_url)

class TweetCreateView(FormUserNeededMixin, CreateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = "tweets/create_view.html"
    # success_url = reverse_lazy('tweet:detail')
    # login_url = '/admin/'
    # fields = [ 'user', 'content']

    # def form_valid(self, form):
    #     if self.request.user.is_authenticated():
    #         form.instance.user = self.request.user
    #         return super(TweetCreateView, self).form_valid(form)
    #     else:
    #         form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue"])
    #         return self.form_invalid(form)

# def Tweet_Create_View(request):
#     form = TweetModelForm(request.POST or None)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instant.user = request.user
#         instance.save()
#     context = {
#     "form": form
#     }
#     return render(request, 'tweets/create_view.html', context)

# Update

class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset= Tweet.objects.all()
    form_class = TweetModelForm
    template_name = "tweets/update_view.html"
    # success_url = reverse_lazy('tweet:detail')

# delete

class TweetDeleteView(LoginRequiredMixin, UserOwnerMixin, DeleteView):
    model = Tweet
    template_name = "tweets/delete_confirm.html"
    success_url = reverse_lazy('tweet:list') # reverse()


# retreive

class TweetDetailView(DetailView):
    template_name = "tweets/tweet_detail.html"
    queryset = Tweet.objects.all()



    # def get_object(self):
    #     # pk = self.kwargs["pk"] key error
    #     pk = self.kwargs.get("pk")
    #     obj = get_object_or_404(Tweet, pk=pk)
    #     # print(pk)
    #     # print(self.kwargs)
    #     # return Tweet.objects.get(id=pk)
    #     return obj

class TweetListView(LoginRequiredMixin, ListView):
    # template_name = "tweets/list_view.html"
    # queryset = Tweet.objects.all()


    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all().order_by('-updated')


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


    def get_context_data(self, *args, **kwargs):

        context = super(TweetListView, self).get_context_data(*args, **kwargs)

        context["create_form"] = TweetModelForm
        context["create_url"] = reverse_lazy("tweet:create")

        # context["another_list"] = Tweet.objects.all()
        # print(context)

        return context



def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')
    else:
        return render(request, 'tweets/template.html', {'timezones': pytz.common_timezones})

# def tweet_detail_view(request, pk=None): # pk = id
#     # obj = Tweet.objects.get(pk=pk) # query to get from database
#     obj = get_object_or_404(Tweet, pk=pk)
#     print(obj)
#     context = {
#         "object": obj,
#
#     }
#     return render(request, "tweets/detail_view.html", context)


# def tweet_detail_view(request, id=1):
#     obj = Tweet.objects.get(id=id) # query to get from database
#     print(obj)
#     context = {
#         "object": obj,
#         "abc": obj
#     }
#     return render(request, "tweets/detail_view.html", context)
#
#
#
# def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     print(queryset)
#     context = {
#         "object_list": queryset
#     }
#     return render(request, "tweets/list_view.html", context)
