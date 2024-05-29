from django.db import models

# Create your models here.

class Catagory(models.Model):
    CatagoryName = models.CharField(max_length=25)
    
    def __str__(self):
        return self.catagory_name