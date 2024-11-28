from django.db import models

class Filamento(models.Model):
    marca = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    color = models.CharField(max_length=50)
    restante = models.IntegerField()
    valor = models.FloatField(max_length=10)

    def __str__(self):
        return f"{self.marca} - {self.tipo} - {self.color}"

class Material(models.Model):
    material = models.CharField(max_length=100)
    valor = models.FloatField(max_length=10)

    def __str__(self):
        return self.material
