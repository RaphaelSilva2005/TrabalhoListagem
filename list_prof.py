from django.shortcuts import render
from .models import Professor

def lista_professores(request):
    professores = Professor.objects.all()
    return render(request, 'lista_professores.html', {'professores': professores})
