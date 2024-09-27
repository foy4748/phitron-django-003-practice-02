from django.shortcuts import get_object_or_404, redirect, render

from album.forms import AddAlbumForm
from album.models import Album


# Create your views here.
def ShowAddAlbumForm(req):
    if req.POST:
        current_form = AddAlbumForm(req.POST)
        if current_form.is_valid():
            current_form.save()
            return redirect("album:all_albums")
    form = AddAlbumForm()
    return render(req, "album/add_album_form.html", {"form": form})


def EditAlbum(req, pk):
    album_instance = get_object_or_404(Album, pk=pk)
    if req.POST:
        current_form = AddAlbumForm(req.POST, instance=album_instance)
        if current_form.is_valid():
            current_form.save()
            return redirect("album:all_albums")
    form = AddAlbumForm(instance=album_instance)
    return render(req, "album/add_album_form.html", {"form": form})


def DeleteAlbum(_, pk):
    album_instance = get_object_or_404(Album, pk=pk)
    album_instance.delete()
    return redirect("album:all_albums")


def ShowAlbums(req):
    albums = Album.objects.all()
    return render(req, "album/albums.html", {"albums": albums})
