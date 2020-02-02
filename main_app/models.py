from django.db import models

class Score(models.Model):
    name = models.CharField(max_length=50)
    points = models.IntegerField()
