from django import forms

class HeroeForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    alias = forms.CharField(max_length=100)
    ciudad = forms.CharField(max_length=100)

class VillanoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    enemigo = forms.CharField(max_length=100)

class ComicForm(forms.Form):
    titulo = forms.CharField(max_length=100)
    heroe = forms.CharField(max_length=100)
    anio = forms.IntegerField()

class BuscarHeroeForm(forms.Form):
    nombre = forms.CharField(max_length=100)