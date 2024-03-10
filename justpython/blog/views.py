from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Post, Category
from django.db.models import Q

# Create your views here.

class BlogListView(generic.ListView):
    template_name = "blog/blog.html"
    queryset = Post.objects.filter(status=Post.ACTIVE)
    print(queryset)
    
class BlogDetailView(generic.DetailView):  
    model = Post
    template_name = "blog/detail.html"
    context_object_name = "post"
    
class BlogCategoryView(generic.ListView):
    template_name = "blog/category.html"
    model = Post
    
    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return category.Category.filter(status=Post.ACTIVE)
    
class BlogSearchView(generic.ListView):
    template_name = "blog/search.html"
    model = Post
    
    def get_queryset(self):
        query = self.request.GET.get('query', '')
        return Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))