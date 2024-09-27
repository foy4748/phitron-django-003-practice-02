from django.urls import path
from musician import views

app_name = "musician"
urlpatterns = [
    path("", views.ShowMusicians, name="all_musicians"),
    path("add/", views.ShowAddMusicianForm, name="add_musician_form"),
    path("edit/<str:pk>", views.EditMusician, name="edit_musician"),
    path("delete/<str:pk>", views.DeleteMusician, name="delete_musician"),
]
