from django.shortcuts import render
from django.http import HttpResponse

from .models import Categoria
from .models import Anuncio

def home(request):
    categorias = Categoria.objects.all()

    ultimosAnuncios = Anuncio.objects.all()[:12]


    return render(request, "home.html", {
        'categorias': categorias,
        'anuncios': ultimosAnuncios,

    })

