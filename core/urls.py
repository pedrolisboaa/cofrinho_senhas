from django.urls import path
from .views import index, login, cadastro, plataforma


urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('cadastro/',cadastro, name='cadastro' ),
    path('plataforma/', plataforma, name='plataforma'),
]

