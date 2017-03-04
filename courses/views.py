from django.shortcuts import render
from courses.models import Course


def courses(request):
    all_courses = Course.objects.all().order_by('-id')
    return render(request, 'courses.html', {'courses': all_courses})
