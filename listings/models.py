from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Band(models.Model):

    name = models.CharField(max_length=100)
    biography = models.TextField(max_length=1000)
    year_formed = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2021)])
    active = models.BooleanField(default=True)
    official_homepage = models.URLField(null=True, blank=True)

    class Genre(models.TextChoices):
        HIP_HOP = "HH"
        SYNTH_POP = "SP"
        ALTERNATIVE_ROCK = "AR"

    genre = models.CharField(choices=Genre.choices, max_length=5)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Band'
        verbose_name_plural = 'Bands'


class Listings(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    sold = models.BooleanField(default=False)
    year = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2021)])
    band = models.ForeignKey(
        Band, null=True, on_delete=models.SET_NULL)

    class Genre(models.TextChoices):
        HIP_HOP = "Misc"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Listing'
        verbose_name_plural = 'Listings'
