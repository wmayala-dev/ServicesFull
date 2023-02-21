from django.shortcuts import render
from rest_framework import generics
from .serializers import CategoriasSerializer, ProductosSerializer
from .models import Categorias, Productos

class ProductosList(generics.ListAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

class CategoriasList(generics.ListAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer

class CategoriasCreate(generics.CreateAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer
    
class CategoriasDelete(generics.DestroyAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer
    lookup_field = "pk"
    
class CategoriasUpdate(generics.UpdateAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer
    lookup_field = "pk"