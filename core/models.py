from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cofre(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    site = models.CharField(max_length=300)
    senha = models.CharField(max_length=298)

    def __str__(self):
        return self.site
