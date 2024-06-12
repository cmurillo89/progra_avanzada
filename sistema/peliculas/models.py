from django.db import models

# Create your models here.
class Pelicula(models.Model):
    id = models.AutoField(primary_key=True , verbose_name="Id")
    titulo = models.CharField(max_length=100 , verbose_name="Título")
    imagen = models.ImageField(upload_to='imagenes/', verbose_name="Imagen", null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True, verbose_name="Descripción")

    def __str__(self):
        fila = str(self.id) + " - " + self.titulo + " - " + self.descripcion
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.delete()
        super().delete()