from django.shortcuts import render
from django.contrib.auth import get_user_model
from.models import Reseña

def lista_reseñas(request):
    reseñas=Reseña.objects.all()
    return render(request, 'Cine/index.html',{'reseñas':reseñas})

def web_historia(request):
    return render(request, 'Cine/Historia.html',{})

def web_categorias(request):
    categorias = [op[0] for op in Reseña.opciones]  
    reseñas_por_categoria = {}

    for categoria in categorias:
        reseñas = Reseña.objects.filter(categoria_pelicula=categoria)
        reseñas_por_categoria[categoria] = reseñas

    return render(request, 'Cine/Categorias.html', {
        'reseñas_por_categoria': reseñas_por_categoria
    })

def web_usuarios(request):
    User = get_user_model()
    usuarios = User.objects.filter(reseña__isnull=False).distinct()
    reseñas_por_usuario = {}

    for usuario in usuarios:
        reseñas = Reseña.objects.filter(user=usuario)
        reseñas_por_usuario[usuario] = reseñas

    return render(request, 'Cine/Usuarios.html', {
        'reseñas_por_usuario': reseñas_por_usuario
    })
    