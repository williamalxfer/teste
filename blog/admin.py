from django.contrib import admin
from .models import Produto
from .models import Mensagem

admin.site.register(Produto)
admin.site.register(Mensagem)


