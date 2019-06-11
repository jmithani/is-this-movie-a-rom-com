from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=256, null=True)
    answer = models.BooleanField(null=True)
    poster_link = models.CharField(max_length=1000, blank=True, null=True)
