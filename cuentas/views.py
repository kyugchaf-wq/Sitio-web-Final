from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

from .forms import RegistroForm
from django.contrib.auth import logout 

def registro(request):
    if request.method == "POST":
        formulario = RegistroForm(request.POST)

        if formulario.is_valid():
            usuario = formulario.save()
            login(request, usuario)

            messages.success(
                request,
                "Tu cuenta se creó correctamente."
            )

            return redirect("catalogo")
    else:
        formulario = RegistroForm()

    return render(
        request,
        "cuentas/registro.html",
        {"formulario": formulario}
    )


def iniciar_sesion(request):
    if request.method == "POST":
        formulario = AuthenticationForm(
            request,
            data=request.POST
        )

        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario)

            messages.success(
                request,
                "Has iniciado sesión correctamente."
            )

            return redirect("catalogo")
    else:
        formulario = AuthenticationForm(request)

    return render(
        request,
        "cuentas/iniciar_sesion.html",
        {"formulario": formulario}
    )
def cerrar_sesion(request):
    if request.method == "POST":
        logout(request)

    return redirect("catalogo")