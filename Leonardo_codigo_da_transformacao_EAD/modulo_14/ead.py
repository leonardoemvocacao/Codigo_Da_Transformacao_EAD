from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.urls import path
from django.contrib import admin
from django.test import TestCase, Client


class Produto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'  


def listar_produtos(request):
    busca = request.GET.get('busca', '')
    lista = Produto.objects.filter(nome__icontains=busca).order_by('nome') if busca else Produto.objects.all().order_by('nome')
    produtos = Paginator(lista, 5).get_page(request.GET.get('page'))
    return render(request, 'produtos/listar.html', {'produtos': produtos, 'busca': busca})

def salvar_produto(request, pk=None):
    obj = get_object_or_404(Produto, pk=pk) if pk else None
    form = ProdutoForm(request.POST or None, instance=obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('listar_produtos')
    return render(request, 'produtos/formulario.html', {'form': form, 'titulo': 'Editar' if pk else 'Cadastrar'})

def deletar_produto(request, pk):
    obj = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('listar_produtos')
    return render(request, 'produtos/confirmar_exclusao.html', {'produto': obj})


urlpatterns = [
    path('', listar_produtos, name='listar_produtos'),
    path('novo/', salvar_produto, name='criar_produto'),
    path('editar/<int:pk>/', salvar_produto, name='editar_produto'),
    path('deletar/<int:pk>/', deletar_produto, name='deletar_produto'),
]


admin.site.register(Produto)


class Testes(TestCase):
    def test_fluxo(self):
        p = Produto.objects.create(nome="A", preco=10, quantidade=1)
        self.assertEqual(Client().get('/').status_code, 200)


"""
<a href="{% url 'criar_produto' %}">Novo Produto</a>
<form method="GET"><input type="text" name="busca" value="{{ busca }}"><button>Buscar</button></form>
<table border="1">
    {% for p in produtos %}
    <tr><td>{{ p.nome }}</td><td>R$ {{ p.preco }}</td><td>
        <a href="{% url 'editar_produto' p.pk %}">Editar</a> | <a href="{% url 'deletar_produto' p.pk %}">Excluir</a>
    </td></tr>
    {% endfor %}
</table>
{% if produtos.has_previous %}<a href="?page={{ produtos.previous_page_number }}&busca={{ busca }}">Anterior</a>{% endif %}
{% if produtos.has_next %}<a href="?page={{ produtos.next_page_number }}&busca={{ busca }}">Próxima</a>{% endif %}

<h1>{{ titulo }}</h1>
<form method="POST">{% csrf_token %}{{ form.as_p }}<button>Salvar</button></form>

<form method="POST">{% csrf_token %}<p>Deletar {{ produto.nome }}?</p><button>Sim</button></form>
"""
