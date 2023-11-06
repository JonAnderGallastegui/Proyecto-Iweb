from django.db import models

# Create your models here.
 
class Departamento(models.Model):
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre

class Habilidad(models.Model):
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre 

class Empleado(models.Model):
    # Campo para la relación one-to-many (un empleado pertenece a un departamento)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    # Campo para la relación many-to-many (un empleado tiene varias habilidades)
    habilidades = models.ManyToManyField(Habilidad)
    nombre = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    # Es posible indicar un valor por defecto mediante 'default'
    antiguedad = models.IntegerField(default=0)
    # Para permitir propiedades con valor null, añadiremos las opciones null=True, blank=True. 
    
    def __str__(self):
        return self.nombre
