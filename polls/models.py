import numbers
from django.db import models

# Create your models here.

class contactUs(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
  #  num = models.IntegerField()
  
  
    def __str__(self):
      return self.name
    

 
 



  
  
