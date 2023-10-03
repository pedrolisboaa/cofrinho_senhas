from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        nome = request.POST.get('nome') 
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmacao_senha = request.POST.get('senha1')

        usuario = User.objects.filter(email=email).first()

        if usuario:
            print('Já existe um usuário com esse login.')
            return render(request, 'cadastro.html')

        usuario = User.objects.create_user(username=nome, email=email, password=senha)
        usuario.save()
        print('Usuário cadastro com sucesso.')
        return render(request, 'cadastro.html')



def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        usuario = authenticate(email=email, password=senha)

        if usuario:
            login_django(request, usuario)
            return HttpResponse('Autenticado')
        else:
            return HttpResponse('Email ou senha inválidos')