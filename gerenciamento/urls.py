from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    
    path('cliente/', views.listar_clientes, name='listar_clientes'),
    path('cliente/create/', views.criar_cliente, name='criar_cliente'),
    path('cliente/edit/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('cliente/delete/<int:pk>/', views.excluir_cliente, name='excluir_cliente'),

    
    path('categoria/', views.listar_categorias, name='listar_categorias'),
    path('categoria/create/', views.criar_categoria, name='criar_categoria'),
    path('categoria/edit/<int:pk>/', views.editar_categoria, name='editar_categoria'),
    path('categoria/delete/<int:pk>/', views.excluir_categoria, name='excluir_categoria'),

    
    path('produto/', views.listar_produtos, name='listar_produtos'),
    path('produto/create/', views.criar_produto, name='criar_produto'),
    path('produto/edit/<int:pk>/', views.editar_produto, name='editar_produto'),
    path('produto/delete/<int:pk>/', views.excluir_produto, name='excluir_produto'),

    
    path('funcionario/', views.listar_funcionarios, name='listar_funcionarios'),
    path('funcionario/create/', views.criar_funcionario, name='criar_funcionario'),
    path('funcionario/edit/<int:pk>/', views.editar_funcionario, name='editar_funcionario'),
    path('funcionario/delete/<int:pk>/', views.excluir_funcionario, name='excluir_funcionario'),

   
    path('mesa/', views.listar_mesas, name='listar_mesas'),
    path('mesa/create/', views.criar_mesa, name='criar_mesa'),
    path('mesa/edit/<int:pk>/', views.editar_mesa, name='editar_mesa'),
    path('mesa/delete/<int:pk>/', views.excluir_mesa, name='excluir_mesa'),

    
    path('pedido/', views.listar_pedidos, name='listar_pedidos'),
    path('pedido/create/', views.criar_pedido, name='criar_pedido'),
    path('pedido/edit/<int:pk>/', views.editar_pedido, name='editar_pedido'),
    path('pedido/delete/<int:pk>/', views.excluir_pedido, name='excluir_pedido'),
]
