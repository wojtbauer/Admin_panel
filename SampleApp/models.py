from django.db import models

# Create your models here.

class SampleModel_1(models.Model):
    text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.text


class SampleModel_2(models.Model):
    text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.text
