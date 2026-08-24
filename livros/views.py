from rest_framework.generics import ListCreateAPIView
from .models import Livro
from .serializers import LivroSerializer

class LivroListCreateView(ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer