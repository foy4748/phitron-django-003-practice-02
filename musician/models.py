from django.db import models

from album.models import Album


# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=512)
    last_name = models.CharField(max_length=512)
    email = models.EmailField(max_length=512)
    phone_number = models.CharField(max_length=512)
    instrument_type = models.CharField(max_length=512)
    album = models.ForeignKey(Album, null=True, on_delete=models.SET_NULL)
