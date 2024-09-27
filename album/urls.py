from django.urls import path
from album import views

app_name = "album"
urlpatterns = [
    path("", views.ShowAddAlbumForm, name="add_album_form"),
    path("albums/", views.ShowAlbums, name="all_albums"),
    path("albums/edit/<str:pk>", views.EditAlbum, name="edit_album"),
    path("albums/delete/<str:pk>", views.DeleteAlbum, name="delete_album"),
]
