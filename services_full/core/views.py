from django.shortcuts import render
from rest_framework import generics, status
from .serializers import CategoriasSerializer, ProductosSerializer, ProveedorSerializer
from .models import Categorias, Productos, Proveedor

# Importando  la tabla auth.users
from django.contrib.auth.models import User
import json

# (JsonResponse) Para el full service 
from django.http import HttpResponse, JsonResponse 
from rest_framework.permissions import AllowAny, IsAuthenticated

# Importando  la tabla tokens para seguridad del sitio
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate

# Importar librería para parsear los datos en JSON
from rest_framework.parsers import JSONParser


# Para crear servicios ALL IN ONE
from rest_framework.decorators import api_view


class ProductosList(generics.ListAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

class ProductosCreate(generics.CreateAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
    
class ProductosDelete(generics.DestroyAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
    lookup_field = "pk"
    
class ProductosUpdate(generics.UpdateAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
    lookup_field = "pk"


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
    
# Servicio para dar de alta usuarios

class RegistrarUsuarios(generics.CreateAPIView):
    
    permission_classes = (AllowAny,)

    def post(self,request):
    
        #recogiendo la informacion desde el front
        usuario = request.data['username']
        correo = request.data['email']
        contraseña = request.data['password']
        nom = request.data['nombre']
        ape = request.data['apellido']
        admin = request.data['staff']
    
        #registrandola en la base de datos 
        nuevo_usuario = User.objects.create_user(usuario,correo,contraseña)
    
        #especicas los demas campos que deseas grabar
        nuevo_usuario.first_name = nom
        nuevo_usuario.last_name = ape
        nuevo_usuario.is_staff = admin
        nuevo_usuario.save()

        #genero el token del usuario registrado anteriormente
        token_usuario = Token.objects.create(user = nuevo_usuario)
        msg = {
            'detail':'Usuario Creado Correctamente con el Token ' + token_usuario.key
            }

        #convierte la cade de texto msg a Json
        rpta = json.dumps(msg)
        return HttpResponse(rpta, content_type = 'application/json')


class LoginUsuario(generics.CreateAPIView):
    def post(self, request):
        usuario = request.data["username"]
        contraseña = request.data["password"]
        usuario = authenticate(username = usuario,password = contraseña)
        if usuario:
            token_usuario = Token.objects.get(user_id = usuario.id)
            msg = {
                "nombre" : usuario.first_name,
                "apellido" : usuario.last_name,
                "correo" : usuario.email,
                "key" : token_usuario.key
            }
        else:
                msg = {
                    'error':'Credenciales Invalidas'
                    }
                
        rpta = json.dumps(msg)
        return HttpResponse(rpta, content_type = 'application/json')  

# Servicio que permite hacer todos los servicios

@api_view(['GET','POST'])
def proveedor_full_service(request):
    
    if request.method == 'GET':
        proveedores = Proveedor.objects.all()
    
    elif request.method == 'POST':
        provee_data = JSONParser().parse(request)
        provee_serializer = ProveedorSerializer(data = provee_data)
        
        if provee_serializer.is_valid():
            provee_serializer.save()
            return JsonResponse(provee_serializer.data, status = status.HTTP_201_CREATED)
        
        return JsonResponse(provee_serializer.errors, status = status.HTTP_400_BAD_REQUEST)    
    
    provee_serializer = ProveedorSerializer(proveedores, many = True) 
    return JsonResponse(provee_serializer.data, safe = False) 

#Crear un servicio que me permita relaizar el GET DETalle

@api_view(['GET','DELETE','PUT'])
def proveedor_service_detail(request,pk):
    
    #seleccionado el proveedor que mostrare en el detalle
    proveedor=Proveedor.objects.get(id = pk)
    
    if request.method == 'GET':
        provee_serializer=ProveedorSerializer(proveedor) 
        return JsonResponse(provee_serializer.data)
    
    elif request.method == 'DELETE':
        proveedor.delete()
        return JsonResponse({
            'Message' : 'El Proveedor se eliminó con éxito'
            },
            status = status.HTTP_200_OK
        )
    
    elif request.method == 'PUT':
        provee_data = JSONParser().parse(request)
        provee_serializer = ProveedorSerializer(proveedor, data = provee_data)
        
        if provee_serializer.is_valid():
            provee_serializer.save()
            return JsonResponse(provee_serializer.data)
        
        return JsonResponse(provee_serializer.errors, status = status.HTTP_400_BAD_REQUEST) 