from django.shortcuts import render

# Create your views here.
def renderListado(request):
    return render(request, 'appTemplate/listado.html')