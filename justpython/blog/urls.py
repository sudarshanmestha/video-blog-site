from django.urls import path
from .views import BlogListView, BlogDetailView
from blog.views import detail
app_name = "blog"

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_post'),
    # path('search/', BlogSearchView.as_view(), name='search'),
    # path('<slug:slug>/', BlogCategoryView.as_view(), name='category_detail'),
    path("<slug:category_slug>/<slug:slug>/", BlogDetailView.as_view(), name='blog_detail'),
]