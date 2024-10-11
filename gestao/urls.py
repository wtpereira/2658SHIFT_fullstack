from django.urls import path

from . import views

app_name = 'gestao'

urlpatterns = [
    path('', views.index, name='index'),
    # path('cadastrar/', views.cadastrar, name='cadastrar'),
    # path('salvar/', views.save, name='save'),
    path('salvar/', views.CadastrarView.as_view(), name='save'),
    # path('listar/', views.listar, name='listar'),
    path('listar/', views.ListarView.as_view(), name='listar'),
    # path('livro/<int:livro_id>', views.view, name='view'),
    path('livro/<int:pk>', views.DetailView.as_view(), name='view'),
    path('teste/', views.teste, name='teste'),
]
