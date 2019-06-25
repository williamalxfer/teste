# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import Produto
from .models import Mensagem

from .forms import FormMensagem
from .forms import FormProduto
from .forms import FormLogin

from datetime import datetime 
from django.http import HttpResponse   
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
   data = datetime.now()
   if data.hour >= 6 and data.hour < 12:
      x = "Bom dia!"
   elif data.hour >= 12 and data.hour <= 18:
      x = "Boa tarde!"
   else:
      x = "Boa noite!"

   y = data.day

   contexto = {'x': x, 'y': y}
   return render(request, 'blog/sobre.html', contexto)


def visualizacoes(request):
   lista_produtos = Produto.objects.order_by("-visualizacoes")[0:5]
   contexto = {'lista_produtos': lista_produtos}
   return render(request, 'blog/produtos.html', contexto)

def melhoravaliado(request):
   #Verificacao de autenticacao
   if request.user.is_authenticated == False:
      form = FormLogin()
      contexto = {"form": form, "mensagem": "Apenas usuários logados podem ver as avaliações."}
      return render(request, 'blog/autenticacao.html', contexto)
      
   lista_produtos = Produto.objects.order_by("-curtidas")[0:3]
   contexto = {'lista_produtos': lista_produtos}
   return render(request, 'blog/avaliacoes.html', contexto)

def pioravaliado(request):
   #Verificacao de autenticacao
   if request.user.is_authenticated == False:
      form = FormLogin()
      contexto = {"form": form, "mensagem": "Apenas usuários logados podem ver as avaliações."}
      return render(request, 'blog/autenticacao.html', contexto)
      
   lista_produtos = Produto.objects.order_by("-descurtidas")[0:3]
   contexto = {'lista_produtos': lista_produtos}
   return render(request, 'blog/avaliacoes.html', contexto)


def sobre(request):
   data = datetime.now()
   if data.hour >= 6 and data.hour < 12:
      x = "Bom dia!"
   elif data.hour >= 12 and data.hour <= 18:
      x = "Boa tarde!"
   else:
      x = "Boa noite!"

   y = data.day

   contexto = {'x': x, 'y': y}
   return render(request, 'blog/sobre.html', contexto)


def teste(request, x,y):
   soma = x + y
   return HttpResponse("A soma de x e y é " + str(soma))

   
def detalhe_produto(request, x):
   #Verificacao de autenticacao
   if request.user.is_authenticated == False:
      form = FormLogin()
      contexto = {"form": form, "mensagem": "Apenas usuários logados podem fazer compras."}
      return render(request, 'blog/autenticacao.html', contexto)
      
   p = Produto.objects.get(id=x)
   p.visualizacoes = p.visualizacoes + 1
   p.save()
   contexto = {"p":p}
   return render(request, 'blog/detalhe_produto.html', contexto)

def curtir(request, x):
   #Verificacao de autenticacao
   if request.user.is_authenticated == False:
      form = FormLogin()
      contexto = {"form": form, "mensagem": "Apenas usuários logados podem avaliar um produtos."}
      return render(request, 'blog/autenticacao.html', contexto)
      
   p = Produto.objects.get(id=x)
   p.curtidas = p.curtidas + 1
   p.save()
   return HttpResponseRedirect("/blog/"+str(x)+"/detalhe_produto")
   
def descurtir(request, x):
   #Verificacao de autenticacao
   if request.user.is_authenticated == False:
      form = FormLogin()
      contexto = {"form": form, "mensagem": "Apenas usuários logados podem avaliar um produto."}
      return render(request, 'blog/autenticacao.html', contexto)
      
   p = Produto.objects.get(id=x)
   p.descurtidas = p.descurtidas + 1
   p.save()
   return HttpResponseRedirect("/blog/"+str(x)+"/detalhe_produto")
   
def comprar(request, x):
   #Verificacao de autenticacao
   if request.user.is_authenticated == False:
      form = FormLogin()
      contexto = {"form": form, "mensagem": "Apenas usuários logados podem fazer compras."}
      return render(request, 'blog/autenticacao.html', contexto)
      
   p = Produto() 
   p = Produto.objects.get(id=x)
   p.quantidade = p.quantidade - 1
   p.save()
   return HttpResponseRedirect('/blog/produtos')



def excluir(request, x):
   #Verificacao de autenticacao
   if request.user.is_authenticated == False:
      form = FormLogin()
      contexto = {"form": form, "mensagem": "Apenas administrador logados podem excluir produtos."}
      return render(request, 'blog/autenticacao.html', contexto)
      
   p = Produto() 
   p = Produto.objects.get(id=x).delete()
   return HttpResponseRedirect('/blog/produtos')


def produtos(request):
   #Verificacao de autenticacao
   if request.user.is_authenticated == False:
      form = FormLogin()
      contexto = {"form": form, "mensagem": "Apenas usuários logados podem fazer compras."}
      return render(request, 'blog/autenticacao.html', contexto)
      
   lista_produtos = Produto.objects.all() #consulta
   lista_aperitivos = Produto.objects.filter(categoria='Aperitivos')
   lista_bebidas = Produto.objects.filter(categoria='Bebidas')
   lista_biscoitos = Produto.objects.filter(categoria='Biscoitos')
   lista_carnes = Produto.objects.filter(categoria='Carnes')
   lista_massas = Produto.objects.filter(categoria='Massas')
   contexto = {"lista_produtos": lista_produtos, "lista_aperitivos": lista_aperitivos, 'lista_bebidas': lista_bebidas, 'lista_biscoitos': lista_biscoitos, 'lista_carnes': lista_carnes, 'lista_massas': lista_massas} #contexto  
   return render(request, 'blog/produtos.html', contexto)

def nova_mensagem(request):
   #Verificacao de autenticacao
   if request.user.is_authenticated == False:
      form = FormLogin()
      contexto = {"form": form, "mensagem": "Apenas usuários logados podem enviar mensagens."}
      return render(request, 'blog/autenticacao.html', contexto)
      
   if request.method == 'POST':
      form = FormMensagem(request.POST)
      if form.is_valid():
           
          ### Salva a mensagem 
         m = Mensagem()
         m.nome = form.cleaned_data['nome']
         m.texto = form.cleaned_data['texto']
         m.assunto = form.cleaned_data['assunto']
         m.email = form.cleaned_data['email']
         m.save()

         return HttpResponseRedirect('/blog/') 
   else:
      form = FormMensagem() 

   contexto = {"form": form}
   return render(request, 'blog/mensagem.html', contexto)


def novo_produto(request):
   #Verificacao de autenticacao
   if request.user.is_authenticated == False:
      form = FormLogin()
      contexto = {"form": form, "mensagem": "Apenas usuários logados podem cadastrar produtos."}
      return render(request, 'blog/autenticacao.html', contexto)
      
   if request.method == 'POST':
      #Tratar os dados vindos do formulário
      form = FormProduto(request.POST)
      if form.is_valid():
         #Salvando um novo post
         p = Produto() 
         p.nome = form.cleaned_data['nome']
         p.marca = form.cleaned_data['marca']
         p.descricao = form.cleaned_data['descricao']
         p.unidade = form.cleaned_data['unidade']
         p.categoria = form.cleaned_data['categoria']
         p.valor = form.cleaned_data['valor']
         p.quantidade = form.cleaned_data['quantidade']
         p.foto = form.cleaned_data['foto']
         p.data_cadastro = form.cleaned_data['data_cadastro']
         p.save()
         return HttpResponseRedirect('/blog/produtos')
      else:
         return HttpResponse("Formulário inválido")
   else:
      #Exibir o formulário (Vindo do GET)
      form = FormProduto()
      contexto = {"form": form}
      return render(request, 'blog/novo_produto.html', contexto)
      

def autenticar(request):
   if request.method == 'POST':
      #Tratar os dados vindos do formulário
      form = FormLogin(request.POST)
      if form.is_valid():
         username = form.cleaned_data['usuario']
         senha = form.cleaned_data['senha']
         
         #Autenticar
         usuario = authenticate(request, username=username, password=senha)
         if usuario is not None:
            login(request, usuario) #Mantém o usuário logado
            return HttpResponseRedirect('/blog/produtos')
         else:
            contexto = {"form": form, "mensagem": "Usuário ou senha inválida" }
            return render(request, 'blog/autenticacao.html', contexto)
      else:
         return HttpResponse("Formulário inválido")
   else:
      #Exibir o formulário (Vindo do GET)
      form = FormLogin()
      contexto = {"form": form}
      return render(request, 'blog/autenticacao.html', contexto)


def sair(request):
    logout(request)
    return HttpResponseRedirect('/blog/')
    




    
