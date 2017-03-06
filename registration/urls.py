from django.conf.urls import url
from registration.views import login_view, login_user, logout_view, register_view, register_user, profile

urlpatterns = [
    url(r'^login/$', login_view, name='login'),
    url(r'^login/user/$', login_user, name='login_user'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^register/$', register_view, name='register'),
    url(r'^register/user/$', register_user, name='register_user'),
    url(r'^profile/(?P<username>\w+)/', profile, name='profile'),
]
