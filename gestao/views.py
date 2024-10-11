from django.shortcuts import get_object_or_404, HttpResponseRedirect, render
from django.urls import reverse_lazy
from django.views import generic
from .models import Livro

def index(request):
    return render(request, 'gestao/pagina.html')

class CadastrarView(generic.CreateView):
    model = Livro
    template_name = 'gestao/form.html'
    success_url = reverse_lazy('gestao:index')
    fields = ['titulo', 'paginas']

# def cadastrar(request):
#     return render(request, 'gestao/form.html')

# def save(request):
#     titulo = request.POST.get('titulo')
#     paginas = int(request.POST.get('paginas'))
#     livro = Livro(titulo=titulo, paginas=paginas)
#     livro.save()
#     return HttpResponseRedirect(reverse('gestao:index'))

class ListarView(generic.ListView):
    template_name = 'gestao/list.html'
    context_object_name = 'livros'

    def get_queryset(self):
        return Livro.objects.all()

# def listar(request):
#     livros = Livro.objects.all()
#     return render(request, 'gestao/list.html', {'livros': livros})


class DetailView(generic.DetailView):
    model = Livro
    template_name = 'gestao/view.html'


# def view(request, livro_id):
#     # livro = Livro.objects.get(id=livro_id)
#     livro = get_object_or_404(Livro, pk=livro_id)
#     return render(request, 'gestao/view.html', { 'livro': livro })

def teste(request):
    return render(request, 'gestao/base_gestao.html')
