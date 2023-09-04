from django.db import models


# Create your models here.


class Inmuebles(models.Model):
    idinmueble = models.IntegerField(unique=True, primary_key=True)
    nombre = models.CharField(max_length=20)
    tipoInmueble = models.CharField(max_length=20)

