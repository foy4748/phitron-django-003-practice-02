from django import forms

from album.models import Album


class AddAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"
        widgets = {
            "album_release_date": forms.DateInput(attrs={"type": "date"}),
            "rating": forms.Select(),
        }
