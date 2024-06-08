from django.shortcuts import render
from musician.models import Musician
from album.models import Album


def home(request):
    # output1 = Album.objects.all()
    output = Musician.objects.all()
    return render(request, 'home.html', {'data': output})
