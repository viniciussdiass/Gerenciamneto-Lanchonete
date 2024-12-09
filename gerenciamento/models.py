from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    endereco = models.TextField()

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cargo = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    data_contratacao = models.DateField()

    def __str__(self):
        return self.nome

class Mesa(models.Model):
    numero = models.PositiveIntegerField(unique=True)
    capacidade = models.PositiveIntegerField()
    ocupada = models.BooleanField(default=False)

    def __str__(self):
        return f"Mesa {self.numero} - {'Ocupada' if self.ocupada else 'Livre'}"

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, null=True, blank=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)
    preco_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    descricao = models.TextField(blank=True, null=True)  

    def __str__(self):
        return f"Pedido {self.id} - {self.data_pedido.strftime('%d/%m/%Y %H:%M')}"

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade}x"
