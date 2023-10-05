from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .util import gerador_de_senha


# Create your views here.

def index(request):
    return render(request, 'index.html')


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        login = request.POST.get('login') 
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmacao_senha = request.POST.get('senha1')

        usuario = User.objects.filter(username=login).first()
        email = User.objects.filter(email=email).first()

        # Protegendo meu login
        if not login.strip():
            messages.error(request, 'Login não pode estar em branco.')
            return render(request, 'cadastro.html')

        if senha != confirmacao_senha: 
            messages.error(request, 'As senhas são diferentes.')
            return render(request, 'cadastro.html')

        if usuario is not None or email is not None:
            messages.error(request, 'Já existe um usuário com esse login ou email.')
            return render(request, 'cadastro.html')

        usuario = User.objects.create_user(username=login, email=email, password=senha)
        usuario.save()
        messages.success(request, 'Usuário cadastro com sucesso.')
        return render(request, 'cadastro.html')



def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        
        login = request.POST.get('login')
        senha = request.POST.get('senha')

        usuario = authenticate(username=login, password=senha)

        if usuario:
            login_django(request, usuario)
            return redirect(plataforma)
        else:
            messages.error(request, 'Login ou Senha não conferem.')
            return render(request, 'login.html')


@login_required(login_url='login')
def plataforma(request):
    return render(request, 'plataforma.html')


def gera_senha(request):
    if request.method == 'POST':
        numero_str = request.POST.get('numero')
        caracteres_str = request.POST.get('caracteres')
        letras_str = request.POST.get('letras')

        if numero_str and caracteres_str and letras_str:
            numero = int(numero_str)
            caracteres = int(caracteres_str)
            letras = int(letras_str)
            
            senha = gerador_de_senha(caracteres, numero, letras)
            messages.success(request, f'{senha}')
            

    return render(request, 'gera_senha.html')