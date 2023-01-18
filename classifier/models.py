from django.db import models

class ImagePrediction(models.Model):
    img = models.ImageField()
    predictions = models.CharField(max_length=250)