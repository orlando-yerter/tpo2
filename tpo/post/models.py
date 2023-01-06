from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="Nombre")
    description = models.CharField(max_length=200, verbose_name="Descripcion")
    price = models.IntegerField(verbose_name="Precio")
    image = models.ImageField(verbose_name="Imagen", upload_to ="projects/", null= True, max_length=255, blank=True ) 
    publicationsDate = models.DateField(verbose_name = 'Fecha de publicacion')
    def __str__(self):
        return f"{self.title} | ${self.price} | {self.publicationsDate}"
       