from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        BIKUTSI = 'B'
        POP = 'PP'

    name = models.fields.CharField(max_length=100)
    genre= models.fields.CharField(choices= Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=50)
    year_formed = models.fields.IntegerField( validators=[MinValueValidator(1990),MaxValueValidator(2025)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    # like_new = models.fields.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'

class Listing(models.Model):
    class Types(models.TextChoices):
        Record = 'Re'
        Clothing = 'Cl'
        Posters = 'Po'
        Miscellaneous = 'Mi'
    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=200)
    sold = models.fields.BooleanField(default=True)
    year = models.fields.IntegerField(validators=[MinValueValidator(1990),MaxValueValidator(2025)])
    type = models.fields.CharField(choices= Types.choices, max_length=5)
    band = models.ForeignKey(Band, null=True, on_delete= models.SET_NULL)

    def __str__(self):
        return f'{self.title}'


