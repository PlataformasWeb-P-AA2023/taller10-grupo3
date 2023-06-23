from django.db import models

# Create your models here.


class Parroquia(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30, choices=(('urbana', 'Urbana'), ('rural', 'Rural')))

    def __str__(self):
        return self.nombre

class BarrioCiudadela(models.Model):
    nombre = models.CharField(max_length=30)
    numero_viviendas = models.PositiveIntegerField()
    numero_parques = models.PositiveIntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')))
    numero_edificios = models.PositiveIntegerField()
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre