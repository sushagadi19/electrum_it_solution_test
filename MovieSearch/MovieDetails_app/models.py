from django.db import models

from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=100)
    Year = models.CharField(max_length=100,default='')
    Rated = models.CharField(max_length=100, default='')
    Released = models.CharField(max_length=100,default='')
    Genre = models.CharField(max_length=100,default='')



class Rating(models.Model):
    Source = models.CharField(max_length=100)
    Value = models.CharField(max_length=100)
    Movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="Ratings")


    def __str__(self):
        return f"Rating from {self.Source} to {self.Movie.Title})"