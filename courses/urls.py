from django.conf.urls import url
from courses.views import courses

urlpatterns = [
    url(r'^$', courses, name='courses')
]
