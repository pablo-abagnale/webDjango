from django.db import models

# Create your models here.

class experiencia(models.Model):
    empresa = models.CharField(max_length=30)
    puesto = models.CharField(max_length=60)
    ingreso = models.DateField()
    egreso = models.DateField()
    descripción = models.CharField(max_length=200)

class estudios_formale(models.Model):
    lugar = models.CharField(max_length=20)
    inicio = models.DateField()
    fin = models.DateField(blank=True, null= True)
    estado = models.BooleanField()
    titulo = models.CharField(max_length=50)
    descripción = models.CharField(max_length=200)
    
class skill(models.Model):
    tipo = models.CharField(max_length=20)
    nivel = models.CharField(max_length=20)
    titulo = models.CharField(max_length=50)
    descripción = models.CharField(max_length=200,blank=True, null= True)
    
class hobbi(models.Model):
    actividad = models.CharField(max_length=20)

class dato(models.Model):
    nombre = models.CharField(max_length=20)
    documento = models.IntegerField()
    pasaporte = models.CharField(max_length=20)
    celular = models.CharField(max_length=10)
    mail = models.EmailField()
    fechaNacimiento = models.DateField()