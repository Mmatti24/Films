from django.urls import path 
from . import views 

urlpatterns = [ 
    path('evaluacion2', views.lista_reseñas, name='lista_reseñas'),
    path('historia', views.web_historia, name='web_historia'), 
    path('categorias', views.web_categorias, name='web_categorias'), 
    path('usuarios', views.web_usuarios, name='web_usuarios'), 
] 