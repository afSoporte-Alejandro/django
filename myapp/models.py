from django.db import models

# Create your models here.
# Aqui crearemos las clases de nuestra aplicacion para comunicarnos con la base de datos
class Project(models.Model):
    name = models.CharField(max_length=200)

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    protect = models.ForeignKey(Project, on_delete=models.CASCADE)