from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from musician.forms import AddMusicianForm
from musician.models import Musician


# Create your views here.


class ShowMusicians(ListView):
    model = Musician


class ShowAddMusicianForm(CreateView):
    model = Musician
    form_class = AddMusicianForm
    success_url = reverse_lazy("musician:all_musicians")


class EditMusician(UpdateView):
    model = Musician
    form_class = AddMusicianForm
    success_url = reverse_lazy("musician:all_musicians")


class DeleteMusician(DeleteView):
    model = Musician
    success_url = reverse_lazy("musician:all_musicians")


# def ShowMusicians(req):
#     musicians = Musician.objects.all()
#     for m in musicians:
#         print(m.album)
#     return render(req, "musician/all_musicians.html", {"musicians": musicians})


# def ShowAddMusicianForm(req):
#     if req.POST:
#         current_form = AddMusicianForm(req.POST)
#         if current_form.is_valid():
#             current_form.save()
#             return redirect("musician:all_musicians")
#     form = AddMusicianForm()
#     return render(req, "musician/add_musician_form.html", {"form": form})


# def EditMusician(req, pk):
#     album_instance = get_object_or_404(Musician, pk=pk)
#     if req.POST:
#         current_form = AddMusicianForm(req.POST, instance=album_instance)
#         if current_form.is_valid():
#             current_form.save()
#             return redirect("album:all_albums")
#     form = AddMusicianForm(instance=album_instance)
#     return render(req, "album/add_album_form.html", {"form": form})


# def DeleteMusician(_, pk):
#     album_instance = get_object_or_404(Musician, pk=pk)
#     album_instance.delete()
#     return redirect("album:all_albums")
