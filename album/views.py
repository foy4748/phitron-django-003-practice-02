from django.shortcuts import redirect, render

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


def ShowAlbums(req):
    albums = Album.objects.all()
    return render(req, "album/albums.html", {"albums": albums})
