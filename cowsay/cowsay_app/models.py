from django.db import models

# Create your models here.
class Cowsay(models.Model):
    cowsay = models.TextField()

    def __str__(self):
        return self.name