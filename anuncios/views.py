from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Categoria
from .models import Anuncio

def home(request):
    categorias = Categoria.objects.all()

    ultimosAnuncios = Anuncio.objects.all()[:12]


    return render(request, "home.html", {
        'categorias': categorias,
        'anuncios': ultimosAnuncios,

    })

def categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    
    categorias = Categoria.objects.all()
    

    Anuncios = Anuncio.objects.filter(categoria=categoria)


    return render(request, "home.html", {
        'categorias': categorias,
        'anuncios': Anuncios,
        'categoria': categoria,
    })