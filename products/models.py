from django.db import models

class Product(models.Model):
    title = models.CharField(max_lenght=512)
    price = models.FloatField()
    category = models.CharField(max_length=255)
    description = models.TextField()
    image=models.CharField(max_length=2083)

    def __str__(self):
        return self.title

