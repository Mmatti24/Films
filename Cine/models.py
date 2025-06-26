from django.db import models
from django.conf import settings

class Reseña(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    nombre_pelicula =  models.CharField(max_length=100)

    opciones = [
            ('Terror','Terror'),
            ('Comedia','Comedia'),
            ('Romance','Romance'),
            ('Fantasía','Fantasía'),
            ('Thriller','Thriller'),
            ('Infantil','Infantil'),
            ('Drama','Drama'),
            ('Triste','Triste'),
            ('Animadas','Animadas'),
            ('Deportes','Deportes'),
        ]
    
    categoria_pelicula = models.CharField(max_length=20, choices=opciones)

    lanzamiento_pelicula = models.DateField()

    reseña_pelicula = models.TextField()

    def __str__(self):
        return self.nombre_pelicula
