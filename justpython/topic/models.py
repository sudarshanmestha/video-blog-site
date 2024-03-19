from django.db import models
from django.shortcuts import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field

class Category(models.Model):
    name = models.CharField(unique=False, max_length=100)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to="thumnails/")
    description = models.TextField()
  
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('topic:post-list', kwargs={"slug": self.slug}) 
    
class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    body = CKEditor5Field(null=True, blank=True, config_name='extends')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=1)
    
    
    class Meta:
        ordering = ["order"]

    
    
    def __str__(self):
        return self.title  
    
    def get_absolute_url(self):
        return reverse('topic:post-detail', kwargs={
            "post_slug": self.slug,
            "slug": self.category.slug
            })  
    
       
    
def set_slug_Category(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)

def set_slug_post(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(set_slug_Category, sender=Category)    
pre_save.connect(set_slug_post, sender=Post)  
