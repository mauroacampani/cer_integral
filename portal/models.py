from django.contrib.auth.models import AbstractUser
from django.db import models
from cer.settings import MEDIA_URL, STATIC_URL



class Users(AbstractUser):
    imagen = models.ImageField(upload_to='usuarios', null=True, blank=True)

    
    def get_imagen(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(MEDIA_URL, '/usuarios/mauro.jpg')
    

class Ocupacion(models.Model):
    nombre = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Ocupacion'
        verbose_name_plural = 'Ocupaciones'
    


class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'

class Profesional(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    ocupacion = models.ForeignKey(Ocupacion, on_delete=models.SET_NULL, null=True)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.SET_NULL, null=True)
    direccion = models.CharField(max_length=255, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    dni = models.CharField(max_length=20, unique=True)
    matricula_profesional = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.ocupacion}"
    
    class Meta:
        verbose_name = 'Profesional'
        verbose_name_plural = 'Profesionales'