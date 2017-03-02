from django.conf.urls import url
from registration.views import login_view
from registration.views import register_view

urlpatterns = [
    url(r'^login/$', login_view, name='login'),
    url(r'^register/$', register_view, name='register'),
]
