# gestao/urls.py
from django.urls import path
from .views import (
    ColaboradorListView, ColaboradorCreateView,
    ColaboradorUpdateView, ColaboradorDeleteView,
    EquipamentoListView, EquipamentoCreateView,
    EquipamentoUpdateView, EquipamentoDeleteView,
    UserListView, UserCreateView, UserUpdateView, UserDeleteView,
    EmprestimoListView, EmprestimoCreateView,
    EmprestimoDevolucaoView, home
)

urlpatterns = [
    path('', home, name='home'),

    # Rota para Listar (Read)
    path('colaboradores/', ColaboradorListView.as_view(), name='colaborador_list'),

    # Rota para Criar (Create)
    path('colaboradores/novo/', ColaboradorCreateView.as_view(), name='colaborador_create'),

    # Rota para Atualizar (Update)
    # <int:pk> significa que esperamos um ID (Primary Key) inteiro
    path('colaboradores/<int:pk>/editar/', ColaboradorUpdateView.as_view(), name='colaborador_update'),

    # Rota para Excluir (Delete)
    path('colaboradores/<int:pk>/excluir/', ColaboradorDeleteView.as_view(), name='colaborador_delete'),

    path('equipamentos/', EquipamentoListView.as_view(), name='equipamento_list'),
    path('equipamentos/novo/', EquipamentoCreateView.as_view(), name='equipamento_create'),
    path('equipamentos/<int:pk>/editar/', EquipamentoUpdateView.as_view(), name='equipamento_update'),
    path('equipamentos/<int:pk>/excluir/', EquipamentoDeleteView.as_view(), name='equipamento_delete'),

    # --- NOVAS ROTAS DE USUÁRIOS ---
    path('usuarios/', UserListView.as_view(), name='user_list'),
    path('usuarios/novo/', UserCreateView.as_view(), name='user_create'),
    path('usuarios/<int:pk>/editar/', UserUpdateView.as_view(), name='user_update'),
    path('usuarios/<int:pk>/excluir/', UserDeleteView.as_view(), name='user_delete'),
    path('emprestimos/', EmprestimoListView.as_view(), name='emprestimo_list'),
    path('emprestimos/novo/', EmprestimoCreateView.as_view(), name='emprestimo_create'),
    path('emprestimos/<int:pk>/devolver/', EmprestimoDevolucaoView.as_view(), name='emprestimo_devolver'),
]