from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=70)
    post_code = models.CharField(max_length=10)
    created_on = models.DateTimeField(auto_now_add=True)
