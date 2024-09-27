from django.urls import path
from musician import views

app_name = "musician"
urlpatterns = [
    path("", views.ShowAddMusicianForm, name="add_musician_form"),
]
