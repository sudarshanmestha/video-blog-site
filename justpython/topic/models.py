from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to="thumnails/")
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Posts')
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    body = CKEditor5Field()
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
    
def set_slug_Category(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)

def set_slug_post(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(set_slug_Category, sender=Category)    
pre_save.connect(set_slug_post, sender=Post)  
