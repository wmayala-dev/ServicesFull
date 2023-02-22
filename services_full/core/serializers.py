from .models import Categorias, Productos, Proveedor
from rest_framework import serializers

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'
        
class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'
        
class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'