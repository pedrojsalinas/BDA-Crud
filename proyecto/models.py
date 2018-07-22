from django.db import models

# Create your models here.
class Victima(models.Model):
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=30)
    ocupacion = models.CharField(max_length=30)
    causa = models.CharField(max_length=20)
    def __str__(self):
       return 'id: '+ str(self.id)+' - '+ self.nombres +' '+ self.apellidos

class Agresor(models.Model):
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=30)
    ocupacion = models.CharField(max_length=30)
    def __str__(self):
       return 'id: '+ str(self.id)+' - '+ self.nombres +' '+ self.apellidos

class Relacion(models.Model):
    tipo = models.CharField(max_length=30)
    tiempo = models.CharField(max_length=30)
    agresion_previa = models.CharField(max_length=30)
    agresor = models.ForeignKey(Agresor, on_delete=models.CASCADE)
    victima = models.ForeignKey(Victima, on_delete=models.CASCADE)


class Femicidio(models.Model):
    fecha = models.CharField(max_length=10)
    hora = models.CharField(max_length=10)
    circunstancia = models.CharField(max_length=40)
    tipo_arma = models.CharField(max_length=30)
    testigo = models.CharField(max_length=30)
    agresor = models.ForeignKey(Agresor, on_delete=models.CASCADE)
    victima = models.ForeignKey(Victima, on_delete=models.CASCADE)
