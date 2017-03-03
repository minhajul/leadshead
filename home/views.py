from django.shortcuts import render
from courses.models import Course


def home_page(request):
    courses = Course.objects.all().order_by('-id')[:6]
    return render(request, 'home.html', {'courses': courses})
