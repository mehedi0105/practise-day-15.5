from django.db import models
from django import forms
from musician.models import Musician
# Create your models here.


class Album(models.Model):
    album_name = models.CharField(max_length=20)
    musician_model = models.ForeignKey(
        Musician, on_delete=models.CASCADE)
    album_realise_date = models.DateField()
    rating = models.IntegerField(
        choices=[(i, i) for i in range(1, 6)], default=None)

    def __str__(self):
        return self.album_name
