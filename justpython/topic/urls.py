from django.urls import path
from .views import CategoryListView, CategoryDetailView, PostDetailView

app_name = "topic"

urlpatterns = [
      path('', CategoryListView.as_view(), name='topic-list'),
      path('<slug>/', CategoryDetailView.as_view(), name='post-list'),
      path('<slug>/<post_slug>', PostDetailView.as_view(), name='post-detail'),
]