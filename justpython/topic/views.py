from django.views import generic
from .models import Category

# Create your views here.
class CategoryListView(generic.ListView):
    template_name = 'topic/blog.html'
    queryset = Category.objects.all()