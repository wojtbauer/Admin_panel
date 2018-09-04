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


class Entry_1(models.Model):
    Sample_obj1 = models.ForeignKey('SampleModel_1', on_delete=models.CASCADE)
    text = models.TextField()
    
    class Meta:
        verbose_name_plural = 'entries_1'
        
    def __str__(self):
        return self.text[:50] + "..."
        
class Entry_2(models.Model):
    Sample_obj2 = models.ForeignKey('SampleModel_2', on_delete=models.CASCADE)
    text = models.TextField()
    
    class Meta:
        verbose_name_plural = 'entries_2'
        
    def __str__(self):
        return self.text[:50] + "..."
