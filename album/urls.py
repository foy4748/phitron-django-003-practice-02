from django.urls import path
from album import views

app_name = "album"
urlpatterns = [
    path("", views.ShowAlbums.as_view(), name="all_albums"),
    path("add/", views.ShowAddAlbumForm.as_view(), name="add_album_form"),
    path("edit/<str:pk>", views.EditAlbum.as_view(), name="edit_album"),
    path("delete/<str:pk>", views.DeleteAlbum.as_view(), name="delete_album"),
    # path("", views.ShowAlbums, name="all_albums"),
    # path("add/", views.ShowAddAlbumForm, name="add_album_form"),
    # path("edit/<str:pk>", views.EditAlbum, name="edit_album"),
    # path("delete/<str:pk>", views.DeleteAlbum, name="delete_album"),
]
