
from django.db import models

# Create your models here.

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="Name", max_length=200)
    size = models.CharField(verbose_name="Size", max_length=200)
    observations = models.TextField(verbose_name="Observations", null=True)
    brand = models.CharField(verbose_name="Brand", max_length=200)
    inventory = models.IntegerField(verbose_name="Inventory", default=0)
    image = models.ImageField(verbose_name="Image", upload_to='images/', null=True)
    date = models.DateTimeField(verbose_name="Date")

    def __str__(self):
        return "Nombre: " + self.name + " - " + "Invenatrio: " + str(self.inventory) + " - " "Fecha: " + str(self.date)

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()