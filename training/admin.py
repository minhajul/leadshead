from django.contrib import admin
from training.models import Training


class TrainingAdmin(admin.ModelAdmin):
    list_display = ('course_title', 'user', 'date', 'participant')
    list_filter = ['user', 'participant']


admin.site.register(Training, TrainingAdmin)
