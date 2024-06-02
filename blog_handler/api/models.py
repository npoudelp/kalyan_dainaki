from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Catagory(models.Model):
    catagoryName = models.CharField(max_length=25, unique=True)
    
    def __str__(self):
        return self.catagoryName
    


class Blogs(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    catagory = models.ForeignKey(Catagory, to_field='catagoryName', on_delete=models.CASCADE)
    author = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    blogDate = models.DateTimeField(auto_now_add=True, blank=True)
    image = models.ImageField(upload_to='blog_thumbnails/')
    views = models.IntegerField(default=0, null=True, blank=True)
    
    def __str__(self):
        return self.title