from django.shortcuts import render

# Create your views here.
def renderListado(request):
    return render(request, 'appTemplate/listado.html')

def renderTematica(request):
    return render(request, 'appTemplate/tematica.html')

def renderPerro(request):
    data = {'nombre':'Perro', 'imagen':'perro.jpg','descripcion':'Descripción: El mejor amigo del hombre.', 'valoracion':'Valoración: 6'}
    return render(request, 'appTemplate/tematica.html', data)

def renderGato(request):
    data = {'nombre':'Gato', 'imagen':'gato.jpg','descripcion':'Descripción: Mezcla entre ternura y salvajismo.', 'valoracion':'Valoración: 9'}
    return render(request, 'appTemplate/tematica.html', data)
