from django.shortcuts import render
from .models import Gosto, Foto

def home(request):
    gostos = Gosto.objects.all()
    return render(request, 'home.html', {'gostos': gostos})

def sobre(request):
    foto = Foto.objects.first()  
    return render(request, 'sobre.html', {'foto': foto})
