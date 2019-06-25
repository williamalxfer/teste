from django.urls import path
from . import views

from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

#Associa a função views.index a url 'index'
urlpatterns = [
    path('', views.index, name='index'),
    #path('artigos', views.artigos, name='artigos'),
    path('sobre', views.sobre, name='sobre'),
    #path('ultimos', views.ultimos, name='ultimos'),
    path('visualizacoes', views.visualizacoes, name='visualizacoes'),
    path('<int:x>/<int:y>/teste', views.teste, name='teste'), 
    #path('<int:x>/detalhe', views.detalhe, name='detalhe'),
    path('<int:x>/detalhe_produto', views.detalhe_produto, name='detalhe_produto'),
    path('<int:x>/curtir', views.curtir, name='curtir'), 
    path('<int:x>/descurtir', views.descurtir, name='descurtir'), 
    path('<int:x>/comprar', views.comprar, name='comprar'), 
    path('<int:x>/excluir', views.excluir, name='excluir'),
    path('melhoravaliado', views.melhoravaliado, name='melhoravaliado'),
    path('pioravaliado', views.pioravaliado, name='pioravaliado'),
    path('produtos',views.produtos, name='produtos'), 
    path('nova_mensagem', views.nova_mensagem, name='nova_mensagem'),
    #path('novo_post', views.novo_post, name='novo_post'),
    path('novo_produto', views.novo_produto, name='novo_produto'),
    path('autenticar', views.autenticar, name='autenticar'),
    path('sair', views.sair, name='sair'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)










