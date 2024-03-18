from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Category, Post

# Create your views here.
class CategoryListView(generic.ListView):
    template_name = 'topic/category.html'
    queryset = Category.objects.all()
    
class CategoryDetailView(generic.DetailView):
    template_name = 'topic/post.html'
    queryset = Category.objects.all()

     
class PostDetailView(generic.DetailView):
    template_name = 'topic/post_detail.html'
    
    def get_object(self):
        post = get_object_or_404(Post, slug=self.kwargs["post_slug"])
        return post
    
    
    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs["slug"])
        return category.post.all()
    

    
       