from django.shortcuts import get_object_or_404, redirect, render

from musician.forms import AddMusicianForm
from musician.models import Musician


# Create your views here.
def ShowMusicians(req):
    musicians = Musician.objects.all()
    return render(req, "musician/all_musicians.html", {"musicians": musicians})


def ShowAddMusicianForm(req):
    if req.POST:
        current_form = AddMusicianForm(req.POST)
        if current_form.is_valid():
            current_form.save()
            return redirect("musician:all_musicians")
    form = AddMusicianForm()
    return render(req, "musician/add_musician_form.html", {"form": form})


def EditMusician(req, pk):
    album_instance = get_object_or_404(Musician, pk=pk)
    if req.POST:
        current_form = AddMusicianForm(req.POST, instance=album_instance)
        if current_form.is_valid():
            current_form.save()
            return redirect("album:all_albums")
    form = AddMusicianForm(instance=album_instance)
    return render(req, "album/add_album_form.html", {"form": form})


def DeleteMusician(_, pk):
    album_instance = get_object_or_404(Musician, pk=pk)
    album_instance.delete()
    return redirect("album:all_albums")
