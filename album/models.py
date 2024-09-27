from django.db import models


# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=1024)
    album_release_date = models.DateField()
    RATING_CHOICES = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ]
    rating = models.IntegerField(choices=RATING_CHOICES, default=5)

    def __str__(self):
        return self.album_name
