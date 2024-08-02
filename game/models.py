from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre)
    data = models.DateField(default='2000-01-01')  # Додано значення за замовчуванням
    rating = models.DecimalField(max_digits=10, decimal_places=2)  # Додано значення за замовчуванням

    def __str__(self):
        return self.title