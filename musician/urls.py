from django.urls import path
from musician import views

app_name = "musician"
urlpatterns = [
    path("", views.ShowMusicians.as_view(), name="all_musicians"),
    path("add/", views.ShowAddMusicianForm.as_view(), name="add_musician_form"),
    path("edit/<str:pk>", views.EditMusician.as_view(), name="edit_musician"),
    path("delete/<str:pk>", views.DeleteMusician.as_view(), name="delete_musician"),
    # path("", views.ShowMusicians, name="all_musicians"),
    # path("add/", views.ShowAddMusicianForm, name="add_musician_form"),
    # path("edit/<str:pk>", views.EditMusician, name="edit_musician"),
    # path("delete/<str:pk>", views.DeleteMusician, name="delete_musician"),
]
