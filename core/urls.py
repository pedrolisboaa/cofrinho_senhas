from django.urls import path
from .views import index, login, cadastro, plataforma, gera_senha


urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('cadastro/',cadastro, name='cadastro' ),
    path('plataforma/', plataforma, name='plataforma'),
    path('gera_senha/', gera_senha, name='gera_senha')
]

