from django.urls import path
from .views import index, login, cadastro, plataforma, gera_senha
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('cadastro/',cadastro, name='cadastro' ),
    path('plataforma/', plataforma, name='plataforma'),
    path('gera_senha/', gera_senha, name='gera_senha'),
    path('logout/',  auth_views.LogoutView.as_view(next_page='index'), name='logout'),

]

