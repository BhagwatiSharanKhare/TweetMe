from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns  = [
url(r'^password/change/$',
        auth_views.password_change,
        name='password_change'),
url(r'^password/change/done/$',
        auth_views.password_change_done,
        name='password_change_done'),
url(r'^password/reset/$',
        auth_views.password_reset,
        name='password_reset'),
url(r'^password/reset/done/$',
        auth_views.password_reset_done,
        name='password_reset_done'),
url(r'^password/reset/\
        (?P<uidb64>[0-9A-Za-z_\-]+)/\
        (?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
        name='password_reset_confirm'),

url(r'^password/reset/complete/$',
        auth_views.password_reset_complete,
        name='password_reset_complete'),
]
