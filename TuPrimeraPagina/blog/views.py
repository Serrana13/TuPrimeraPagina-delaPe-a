from django.shortcuts import render

from django.shortcuts import render
from .models import Heroe, Villano, Comic
from .forms import HeroeForm, VillanoForm, ComicForm, BuscarHeroeForm


def inicio(request):
    return render(request, "blog/inicio.html")


def crear_heroe(request):
    if request.method == "POST":
        form = HeroeForm(request.POST)
        if form.is_valid():
            Heroe.objects.create(**form.cleaned_data)
    else:
        form = HeroeForm()
    return render(request, "blog/heroe_form.html", {"form": form})


def crear_villano(request):
    if request.method == "POST":
        form = VillanoForm(request.POST)
        if form.is_valid():
            Villano.objects.create(**form.cleaned_data)
    else:
        form = VillanoForm()
    return render(request, "blog/villano_form.html", {"form": form})


def crear_comic(request):
    if request.method == "POST":
        form = ComicForm(request.POST)
        if form.is_valid():
            Comic.objects.create(**form.cleaned_data)
    else:
        form = ComicForm()
    return render(request, "blog/comic_form.html", {"form": form})


def buscar_heroe(request):
    resultado = None
    if request.method == "POST":
        form = BuscarHeroeForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            resultado = Heroe.objects.filter(nombre__icontains=nombre)
    else:
        form = BuscarHeroeForm()

    return render(request, "blog/buscar.html", {"form": form, "resultado": resultado})