from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Post, Category
from django.db.models import Q

# Create your views here.

class BlogListView(generic.ListView):
    template_name = "blog/blog.html"
    queryset = Post.objects.filter(status=Post.ACTIVE)
    print(queryset)

    
# def detail(request, category_slug, slug):
#     print(category_slug, slug)
#     post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)
#     return render(request, 'blog/detail.html', {'post': post})

class BlogDetailView(generic.DetailView): 
    template_name = "blog/detail.html" 
    model = Post
    context_object_name = "post"

# def category(request, slug):
#     category = get_object_or_404(Category, slug=slug)
#     posts = category.Category.filter(status=Post.ACTIVE)
    
#     return render(request, 'blog/category.html', {'category': category, 'posts': posts})
    
# def search(request):
#     query = request.GET.get('query', '')
#     posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))
    
#     return render(request, 'blog/search.html', {'posts':posts, 'query': query}) 

    
# class BlogCategoryView(generic.ListView):
#     template_name = "blog/category.html"
#     model = Post
    
#     def get_queryset(self):
#         category = get_object_or_404(Category, slug=self.kwargs['slug'])
#         return category.Category.filter(status=Post.ACTIVE)
    
# class BlogSearchView(generic.ListView):
#     template_name = "blog/search.html"
#     model = Post
    
#     def get_queryset(self):
#         query = self.request.GET.get('query', '')
#         return Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))