from django.db import models

# Create your models here.
class taller1 (models.Model):
    titulo=models.CharField(max_length=200)
    contenido=models.TextField()
    imagen=models.ImageField(upload_to="core")
    fechacreacion=models.DateTimeField(auto_now_add=True)
    fechamodificacion=models.DateTimeField(auto_now=True)
