from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        app_label = 'blog'  # Specify the app label
        ordering = ('title',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

            
# Create your models here.
class Post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'
    
    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft')
    )
    
    category = models.ForeignKey(Category, related_name='Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    image = models.ImageField(upload_to = 'uploads/', null='True', blank='True')
    
    
    class Meta:
        ordering = ('-created_at',)
        
    def __str__(self):
        return self.title