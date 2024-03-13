from django.urls import path
from .views import CategoryListView

app_name = "topic"

urlpatterns = [
      path('', CategoryListView.as_view(), name='topic-list'),
]