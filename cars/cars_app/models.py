from django.db import models
from django.core import validators as valid
from .validators import *


class Dealership(models.Model):
    name = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return f"{self.name}"

class Make(models.Model):
    dealer_id = models.ForeignKey(Dealership, on_delete=models.CASCADE, related_name="Make")
    name      = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return f"{self.name}"

class Type(models.Model):
    make_id = models.ForeignKey(Make, on_delete=models.CASCADE, related_name="Type")
    name    = models.CharField(max_length=255, null=False)
    year    = models.IntegerField(validators=[valid.MinValueValidator(1950), valid.MaxValueValidator(2023)])
    color   = models.CharField(max_length=(11))
    
    def __str__(self):
        return f"{self.name} | {self.year} | {self.color}"