from django.db import models

class Persona(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=50)
    apellido = models.TextField(verbose_name="Apellido")
    dni = models.CharField(verbose_name= "DNI", max_length=12)
    mail =models.EmailField(verbose_name="Email", max_length=100)
    apodo = models.CharField(verbose_name= "Apodo", max_length= 100)

    def __str__(self):
        return f"{self.dni} - {self.apellido}"