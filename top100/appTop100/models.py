from django.db import models

 
class Estilo(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
 
class Interprete(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)
    def __str__(self):
        return self.nombre

class Cancion(models.Model):
    titulo = models.CharField(max_length=50)
    estilo = models.ForeignKey(Estilo, on_delete=models.CASCADE)  
    interpretes = models.ManyToManyField(Interprete)
    fecha_lanzamiento = models.DateField(default=None, null=True) 
    duracion = models.IntegerField(default=0)
    posicion = models.IntegerField(default=0)
    def __str__(self):
        return self.titulo
