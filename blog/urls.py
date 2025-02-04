from django.urls import path
from .views import article_list, article_detail

urlpatterns = [
    path('', article_list, name='article-list'),
    path('<int:pk>/', article_detail, name='article-detail'),
]
