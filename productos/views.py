
from django.shortcuts import render
from .models import Producto, Categoria


def catalogo(request):
    productos = Producto.objects.select_related(
        "categoria"
    ).all().order_by("nombre")

    categorias = Categoria.objects.all().order_by("nombre")

    return render(
        request,
        "productos/catalogo.html",
        {
            "productos": productos,
            "categorias": categorias,
        },
    )
