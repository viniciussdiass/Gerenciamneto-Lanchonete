from django.shortcuts import render, redirect, get_object_or_404
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

def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'gerenciamento/cliente/edit.html', {'form': form})

def excluir_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect('listar_clientes')


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

def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'gerenciamento/categoria/edit.html', {'form': form})

def excluir_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    categoria.delete()
    return redirect('listar_categorias')


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

def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'gerenciamento/produto/edit.html', {'form': form})

def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    produto.delete()
    return redirect('listar_produtos')


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

def editar_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('listar_funcionarios')
    else:
        form = FuncionarioForm(instance=funcionario)
    return render(request, 'gerenciamento/funcionario/edit.html', {'form': form})

def excluir_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    funcionario.delete()
    return redirect('listar_funcionarios')


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

def editar_mesa(request, pk):
    mesa = get_object_or_404(Mesa, pk=pk)
    if request.method == 'POST':
        form = MesaForm(request.POST, instance=mesa)
        if form.is_valid():
            form.save()
            return redirect('listar_mesas')
    else:
        form = MesaForm(instance=mesa)
    return render(request, 'gerenciamento/mesa/edit.html', {'form': form})

def excluir_mesa(request, pk):
    mesa = get_object_or_404(Mesa, pk=pk)
    mesa.delete()
    return redirect('listar_mesas')


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

def editar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('listar_pedidos')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'gerenciamento/pedido/edit.html', {'form': form})

def excluir_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    pedido.delete()
    return redirect('listar_pedidos')
