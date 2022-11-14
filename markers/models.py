from django.db import models
from django.contrib.gis.db import models


class Marker(models.Model):
    name = models.CharField(max_length=250)
    location = models.PointField()

    def __str__(self):
        return self.name
    