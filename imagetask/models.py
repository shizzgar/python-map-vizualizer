from django.db import models
from django.contrib.gis.db import models



# Create your models here.
class Counter(models.Model):
    num = models.IntegerField()


class Image(models.Model):
    name = models.CharField(max_length = 255)  
    square = models.PolygonField(null=True)  
    data = models.BinaryField(null=True)

    def __str__(self):
        return self.name




