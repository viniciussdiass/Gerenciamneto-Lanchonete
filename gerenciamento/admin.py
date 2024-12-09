from django.contrib import admin
from .models import Cliente, Categoria, Produto, Funcionario, Mesa, Pedido, ItemPedido

admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Funcionario)
admin.site.register(Mesa)
admin.site.register(Pedido)
admin.site.register(ItemPedido)
