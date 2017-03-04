from django.conf.urls import url
from courses.views import CourseListView, CourseDetailsView

urlpatterns = [
    url(r'^$', CourseListView.as_view(), name='courses'),
    url(r'^details/(?P<pk>[0-9]+)/$', CourseDetailsView.as_view(), name='details'),
]
