from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la Categoria')

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Id')
    nombre = models.CharField(max_length=64, verbose_name='Nombre')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')
    precio = models.IntegerField(verbose_name='Precio')
    descripcion =  models.CharField(max_length=100, verbose_name='Descripcion')

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'