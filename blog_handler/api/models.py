from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Catagory(models.Model):
    catagoryName = models.CharField(max_length=25)
    
    def __str__(self):
        return self.catagoryName
    


class Blogs(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blogDate = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_thumbnails/')
    
    def __str__(self):
        return self.title