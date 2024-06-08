from django.shortcuts import render, redirect
from . import models
from musician.forms import MusicianForm
# Create your views here.


def add_musician(request):
    if request.method == 'POST':
        musician = MusicianForm(request.POST)
        if musician.is_valid():
            musician.save()
            return redirect('home')
    else:
        musician = MusicianForm()
    return render(request, 'add_musician.html', {'form': musician})
    # return render(request, 'home.html')


def edit_album(request, id):
    row = models.Musician.objects.get(pk=id)
    row_line = MusicianForm(instance=row)
    if request.method == 'POST':
        row_line = MusicianForm(request.POST, instance=row)
        if row_line.is_valid():
            row_line.save()
            return redirect('home')
    return render(request, 'add_musician.html', {'form': row_line})


def delete_album(request, id):
    row = models.Musician.objects.get(pk=id)
    row.delete()
    return redirect('home')
