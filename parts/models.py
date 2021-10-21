from django.db import models

# Create your models here.
class Part(models.Model):
    nazwa = models.CharField(max_length=100, null=False)
    opis = models.CharField(max_length=150, null=False)
    ilość = models.IntegerField(default=0)
    kupione_od = models.TextField()
    dodane = models.DateField()