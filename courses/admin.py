from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'fee', 'location', 'duration')
    list_filter = ['fee']
    search_fields = ['title']

admin.site.register(Course, CourseAdmin)
