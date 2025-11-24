from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login

def criar_conta(request):
    if request.method == "POST":
        username = request.POST.get("username")
        nome = request.POST.get("nome")
        sobrenome = request.POST.get("sobrenome")
        email = request.POST.get("email")
        senha1 = request.POST.get("password1")
        senha2 = request.POST.get("password2")

        # Verificação: senhas iguais
        if senha1 != senha2:
            messages.error(request, "As senhas não coincidem.")
            return render(request, "login/criar_conta.html")

        # Verificação: usuário já existe
        if User.objects.filter(username=username).exists():
            messages.error(request, "Esse nome de usuário já está em uso.")
            return render(request, "login/criar_conta.html")

        # Verificação: email já cadastrado
        if User.objects.filter(email=email).exists():
            messages.error(request, "Esse e-mail já está registrado.")
            return render(request, "login/criar_conta.html")

        # Criação do usuário
        user = User.objects.create_user(
            username=username,
            email=email,
            password=senha1,
            
        )

        # Salvar nome e sobrenome
        user.first_name = nome
        user.last_name = sobrenome
        user.save()

        messages.success(request, "Conta criada com sucesso!")

        login(request, user)  # faz login automático
        return redirect("/")  # redireciona para a home

    return render(request, "login/criar_conta.html")
