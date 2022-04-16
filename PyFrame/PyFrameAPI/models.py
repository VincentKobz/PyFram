from django.db import models

# Create your models here.
class Calcul(models.Model):
    calcul_to_parse = models.CharField(max_length=200)