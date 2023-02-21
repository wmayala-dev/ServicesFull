from django.urls import path
from .views import ProductosList, CategoriasList, CategoriasCreate, CategoriasDelete, CategoriasUpdate

#Endpoint
urlpatterns = [
    # path('api/productsall/', ProductosList.as_view()),
    path('api/categoriasall/', CategoriasList.as_view()),
    path('api/categoriascreate/', CategoriasCreate.as_view()),
    path('api/categoriasdelete/<pk>', CategoriasDelete.as_view()),
    path('api/categoriasupdate/<pk>', CategoriasUpdate.as_view()),
]