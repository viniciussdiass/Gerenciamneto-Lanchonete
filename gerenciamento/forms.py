from django import forms
from .models import Cliente, Categoria, Produto, Funcionario, Mesa, Pedido

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'

class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = '__all__'

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
    
    descricao = forms.CharField(widget=forms.Textarea, required=False)  
