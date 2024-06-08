from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from album.forms import AlbumForm
# Create your views here.


def add_album(request):
    if request.method == 'POST':
        album = AlbumForm(request.POST)
        if album.is_valid():
            album.save()
            return redirect('home')
    else:
        album = AlbumForm()
    return render(request, 'add_musician.html', {'form': album})
    # return render(request, 'home.html')


def edit_album(request, id):
    row = models.Album.objects.get(pk=id)
    row_line = AlbumForm(instance=row)
    if request.method == 'POST':
        row_line = AlbumForm(request.POST, instance=row)
        if row_line.is_valid():
            row_line.save()
            return redirect('home')
    return render(request, 'add_musician.html', {'form': row_line})


def delete_album(request, id):
    row = models.Album.objects.get(pk=id)
    row.delete()
    return redirect('home')
