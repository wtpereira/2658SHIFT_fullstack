from django.shortcuts import render
from .models import Livro

def index(request):
    return render(request, 'gestao/pagina.html')

def cadastrar(request):
    return render(request, 'gestao/form.html')

def listar(request):
    livros = Livro.objects.all()
    return render(request, 'gestao/list.html', {'livros': livros})