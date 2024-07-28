from django.db import models

class Vehiculo(models.Model):
    tipo = models.CharField(max_length=20,null=False,primary_key=True)
    marca = models.CharField(max_length=50,null=False)
    modelo = models.CharField(max_length=50,null=False)
    precio = models.IntegerField()
    estado = models.CharField(max_length=50,null=False)
    foto = models.ImageField(null=False,default="ninguno")

    def __str__(self):
        return self.tipo  + "  |  " +self.marca  + "  |  " +self.modelo  + "  |  " 


class Empleado(models.Model):
    nombre = models.CharField(max_length=100,null=False)
    apellido = models.CharField(max_length=100,null=False)
    dni = models.IntegerField()
    numero_telefono = models.CharField(max_length=20,null=False)
    email = models.EmailField()

    def __str__(self):
     return self.nombre + "" + self.apellido   + "  |  " +self.numero_telefono   + "  |  " +self.email


class Cliente(models.Model):
    nombre = models.CharField(max_length=100,null=False)
    apellido = models.CharField(max_length=100,null=False)
    dni = models.IntegerField()
    numero_telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
     return f'{self.nombre + " " + self.apellido  + "  |  " + self.numero_telefono  + "  |  " + self.email}'