from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from album.forms import AddAlbumForm
from album.models import Album
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.
class ShowAddAlbumForm(CreateView):
    model = Album
    form_class = AddAlbumForm
    success_url = reverse_lazy("album:all_albums")


class EditAlbum(UpdateView):
    model = Album
    form_class = AddAlbumForm
    success_url = reverse_lazy("album:all_albums")


class DeleteAlbum(DeleteView):
    model = Album
    success_url = reverse_lazy("album:all_albums")


class ShowAlbums(ListView):
    model = Album


# def ShowAddAlbumForm(req):
#     if req.POST:
#         current_form = AddAlbumForm(req.POST)
#         if current_form.is_valid():
#             current_form.save()
#             return redirect("album:all_albums")
#     form = AddAlbumForm()
#     return render(req, "album/add_album_form.html", {"form": form})


# def EditAlbum(req, pk):
#     album_instance = get_object_or_404(Album, pk=pk)
#     if req.POST:
#         current_form = AddAlbumForm(req.POST, instance=album_instance)
#         if current_form.is_valid():
#             current_form.save()
#             return redirect("album:all_albums")
#     form = AddAlbumForm(instance=album_instance)
#     return render(req, "album/add_album_form.html", {"form": form})


# def DeleteAlbum(_, pk):
#     album_instance = get_object_or_404(Album, pk=pk)
#     album_instance.delete()
#     return redirect("album:all_albums")


# def ShowAlbums(req):
#     albums = Album.objects.all()
#     return render(req, "album/albums.html", {"albums": albums})
