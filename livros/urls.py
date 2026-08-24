from django.urls import path
from .views import LivroListCreateView

urlpatterns = [
    path('', LivroListCreateView.as_view(), name='livros-list-create'),
]