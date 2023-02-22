from django.urls import path
from .views import ProductosList, ProductosCreate, ProductosDelete, ProductosUpdate
from .views import CategoriasList, CategoriasCreate, CategoriasDelete, CategoriasUpdate 
from .views import RegistrarUsuarios, LoginUsuario
from .views import proveedor_full_service, proveedor_service_detail

#Endpoint
urlpatterns = [
    
    # Rutas CRUD de Productos
    path('api/productosall/', ProductosList.as_view()),
    path('api/productoscreate/', ProductosCreate.as_view()),
    path('api/productosdelete/<pk>', ProductosDelete.as_view()),
    path('api/productosupdate/<pk>', ProductosUpdate.as_view()),
    
    # Rutas CRUD de Categorías
    path('api/categoriasall/', CategoriasList.as_view()),
    path('api/categoriascreate/', CategoriasCreate.as_view()),
    path('api/categoriasdelete/<pk>', CategoriasDelete.as_view()),
    path('api/categoriasupdate/<pk>', CategoriasUpdate.as_view()),
    
    # Rutas altas de usuarios
    path('api/registrarusuarios/', RegistrarUsuarios.as_view()),
    
    # Login de usuarios
    path('api/login/', LoginUsuario.as_view()),
    
    # Rutas altas de proveedores
    
    ## Show - Create
    path('api/proveedores_full/', proveedor_full_service),
    
    ## Delete -Update
    path('api/proveedores_detail/<pk>', proveedor_service_detail),
]