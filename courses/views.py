# from django.shortcuts import render
from django.views import generic
from courses.models import Course


class CourseListView(generic.ListView):
    model = Course
    template_name = 'courses.html'
    context_object_name = 'courses'
    paginate_by = 2

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page', self.paginate_by)


class CourseDetailsView(generic.DetailView):
    model = Course
    template_name = 'details.html'
    context_object_name = 'course'

# def courses(request):
#     all_courses = Course.objects.all().order_by('-id')
#     return render(request, 'courses.html', {'courses': all_courses})
