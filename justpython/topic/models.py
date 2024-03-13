from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to="thumnails/")
    
    def __str__(self):
        return self.title
    
class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Posts')
    title = models.CharField(max_length=255)
    body = CKEditor5Field()
    description = models.TextField()
    
    def __str__(self):
        return self.title