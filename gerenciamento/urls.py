from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    
    path('cliente/', views.listar_clientes, name='listar_clientes'),
    path('cliente/create/', views.criar_cliente, name='criar_cliente'),

    
    path('categoria/', views.listar_categorias, name='listar_categorias'),
    path('categoria/create/', views.criar_categoria, name='criar_categoria'),

    
    path('produto/', views.listar_produtos, name='listar_produtos'),
    path('produto/create/', views.criar_produto, name='criar_produto'),

    
    path('funcionario/', views.listar_funcionarios, name='listar_funcionarios'),
    path('funcionario/create/', views.criar_funcionario, name='criar_funcionario'),

    
    path('mesa/', views.listar_mesas, name='listar_mesas'),
    path('mesa/create/', views.criar_mesa, name='criar_mesa'),

   
    path('pedido/', views.listar_pedidos, name='listar_pedidos'),
    path('pedido/create/', views.criar_pedido, name='criar_pedido'),
]
