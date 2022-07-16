from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()
    adress= models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    com = models.CharField(max_length=100)
   
    

    


    

    
