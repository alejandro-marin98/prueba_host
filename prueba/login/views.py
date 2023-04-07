from django.shortcuts import render, redirect
from .forms import RegisterForm, FormularioLogin
# Crear cookie (o token) para identificar usuario
from django.contrib.auth import login, logout
from .models import User
# Considerar el error específico que se de en la BBDD
from django.db import IntegrityError
from solicitudes.models import Solicitudes
from django.http import HttpResponse

from solicitudes.views import isFriendOf, getFriendListsByUsername
from gestionLibros.views import getLibrosByUsername


# from django.http import HttpResponse

# PARA INSERTAR LOS USUARIOS EN LA BASE DE DATOS (NO VERIFICA NADA)
from .models import User


def getAllUsers():
    return list(User.objects.all())

def createUser(request):

    if (request.method == 'GET'):
        print('Enviando formulario...')

        return render(request, 'register.html', {'form': RegisterForm()})
    
    form  = RegisterForm(data=request.POST)

    if form.is_valid():
        user = User(
            username=request.POST['username'],
            password=request.POST['password'],
            email=request.POST['email']
        )
        user.save()
        login(request, user)
        print(user.username)
        return redirect('/')
  
    else:
        return render(request, 'register.html', {'form': form})


def loginUser(request):  
    if (request.method == 'GET'):
        return render(request, 'login.html', {'form': FormularioLogin()}
    )

    print('EL POST', request.POST)

    form = FormularioLogin(data=request.POST)
    
    if form.is_valid():
        usrnm = request.POST.get('username')
        pw = request.POST.get('password')
        user = User.objects.filter(username=usrnm, password=pw)[0]
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'register.html', {'form': form})


def cerrarSesion(request):
    logout(request)
    return redirect('/')

def profile(request):
    
    username = request.POST.get('username')

    if not request.user.is_authenticated and not username:
        return redirect('/login')

    if (not request.user.is_authenticated) and username:
        match = User.objects.filter(username=username)[0]
        return render(request, 'miPerfil.html', {'user': match})

    
    if request.user.is_authenticated and not username:
        libros = getLibrosByUsername(request.user.username)
        return render(request, 'miPerfil.html', {'user': request.user, 'libros': libros, 'mostrar': True})

    match = User.objects.filter(username=username)[0]
    libros = getLibrosByUsername(match.username)
    if match == request.user:
        return render(request, 'miPerfil.html', {'user': match, 'libros': libros, 'mostrar': True})
    
    estado = isFriendOf(username, request.user.username)

    if estado:
        return render(request, 'miPerfil.html', {'user': match, 'libros': libros,  'mostrar': True})
    
    return render(request, 'miPerfil.html', {'user': match, 'libros': libros, 'input': True})

  
def friends(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    def getFriendsAndNotFriendList():
        accepted, pending = getFriendListsByUsername(request.user.username)

        all_users = getAllUsers()

        all_users.remove(request.user)

        filter_user = lambda user: user.username not in [i['usuario'] for i in accepted]

        not_friend_users = list(filter(filter_user, all_users))

        pending_users_names = [i['usuario'] for i in pending]

        filter_status_request = lambda user: [user, 'PENDIENTE'] if user.username in pending_users_names else [user, 'NO_PENDIENTE']

        filtered_not_friends_list = list(map(filter_status_request, not_friend_users))

        return accepted, filtered_not_friends_list

    retrieved_friends, not_friends = getFriendsAndNotFriendList()

    return render(request, 'misAmigos.html', {'amigos': retrieved_friends, 'no_amigos': not_friends})
    

    

