from django.db import models


class Course(models.Model):
    location_choice = (
        ('ACT - Canberra', 'ACT - Canberra'),
        ('NSW - Parramatta', 'NSW - Parramatta'),
        ('NSW - Sydney', 'NSW - Sydney'),
        ('GLD - Brisbane', 'GLD - Brisbane'),
        ('SA - Adelaide', 'SA - Adelaide'),
        ('VIC - Melbourne', 'VIC - Melbourne'),
        ('WA - Perth', 'WA - Perth'),
        ('DH - Dhaka', 'DH - Dhaka'),
    )
    title = models.CharField(max_length=200)
    fee = models.IntegerField()
    location = models.CharField(max_length=100, choices=location_choice)
    duration = models.CharField(max_length=50)
    details = models.TextField(max_length=255)

    def __str__(self):
        return self.title
