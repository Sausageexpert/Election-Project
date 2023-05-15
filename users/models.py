from django.db import models

# Create your models here.

class Students(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    identity = models.CharField(max_length=200)
        
