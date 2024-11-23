from django.core.validators import MinValueValidator
from django.db import models


class Color(models.Model):
    color_name = models.CharField(max_length=50, unique=True)
    hex_code = models.CharField(max_length=7)

    def __str__(self):
        return self.color_name


class Episode(models.Model):
    season_number = models.IntegerField(validators=[MinValueValidator(1)])
    episode_number = models.IntegerField(validators=[MinValueValidator(1)])
    painting_title = models.CharField(max_length=255)
    youtube_src = models.CharField(max_length=255)
    colors = models.ManyToManyField(Color)

    class Meta:
        unique_together = ["season_number", "episode_number"]

    def __str__(self):
        return self.painting_title
