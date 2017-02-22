from django.contrib import admin
from training.models import Training


class TrainingAdmin(admin.ModelAdmin):
    list_filter = ['user']


admin.site.register(Training, TrainingAdmin)
