from django.db import models

# Create your models here.
 
class Estilo(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
 
class Interprete(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    def __str__(self):
        return self.nombre

class Cancion(models.Model):
    titulo = models.CharField(max_length=50)
    estilo = models.ForeignKey(Estilo, on_delete=models.CASCADE)  
    interpretes = models.ManyToManyField(Interprete)
    def __str__(self):
        return self.titulo
