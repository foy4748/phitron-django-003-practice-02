from django.shortcuts import render

from musician.forms import AddMusicianForm


# Create your views here.
def ShowAddMusicianForm(req):
    form = AddMusicianForm()
    return render(req, "musician/add_musician_form.html", {"form": form})
