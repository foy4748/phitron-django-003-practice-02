from django.urls import path
from album import views

app_name = "album"
urlpatterns = [
    path("", views.ShowAlbums, name="all_albums"),
    path("add/", views.ShowAddAlbumForm, name="add_album_form"),
    path("edit/<str:pk>", views.EditAlbum, name="edit_album"),
    path("delete/<str:pk>", views.DeleteAlbum, name="delete_album"),
]
