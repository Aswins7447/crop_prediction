from django.db import models

class Crop(models.Model):
    ph = models.FloatField()
    nitrogen = models.FloatField()
    phosphorous = models.FloatField()
    potassium = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    crop = models.CharField(max_length=255)


    def __str__(self):
        return self.crop
        