from django.shortcuts import render, redirect
from .models import Cliente, Categoria, Produto, Funcionario, Mesa, Pedido
from .forms import ClienteForm, CategoriaForm, ProdutoForm, FuncionarioForm, MesaForm, PedidoForm


def index(request):
    return render(request, 'gerenciamento/index.html')


def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'gerenciamento/cliente/list.html', {'clientes': clientes})

def criar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'gerenciamento/cliente/create.html', {'form': form})


def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'gerenciamento/categoria/list.html', {'categorias': categorias})

def criar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'gerenciamento/categoria/create.html', {'form': form})


def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'gerenciamento/produto/list.html', {'produtos': produtos})

def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'gerenciamento/produto/create.html', {'form': form})


def listar_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'gerenciamento/funcionario/list.html', {'funcionarios': funcionarios})

def criar_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_funcionarios')
    else:
        form = FuncionarioForm()
    return render(request, 'gerenciamento/funcionario/create.html', {'form': form})


def listar_mesas(request):
    mesas = Mesa.objects.all()
    return render(request, 'gerenciamento/mesa/list.html', {'mesas': mesas})

def criar_mesa(request):
    if request.method == 'POST':
        form = MesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_mesas')
    else:
        form = MesaForm()
    return render(request, 'gerenciamento/mesa/create.html', {'form': form})


def listar_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'gerenciamento/pedido/list.html', {'pedidos': pedidos})

def criar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'gerenciamento/pedido/create.html', {'form': form})
