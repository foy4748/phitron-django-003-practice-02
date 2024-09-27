from django import forms

from album.models import Album
from musician.models import Musician


class AddMusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = "__all__"

    album = forms.ModelChoiceField(queryset=Album.objects.all())
