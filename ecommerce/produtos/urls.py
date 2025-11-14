from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('<int:produto_id>/', views.detalhe_produto, name='detalhe_produto'),
    path('inicio/', views.pagina_inicial, name='pagina_inicial'),
]

