from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Libros, Listas, Opiniones
from django.http import HttpResponse

def getLibrosByUsername(username):
    try:
        return Listas.objects.all().select_related('user', 'book').filter(user=username).exclude(estado='sin_guardar')
    except:
        return []

def getOpinionesByIsbn(isbn):
    try:
        opiniones = Opiniones.objects.all().select_related('user', 'book').filter(book=isbn)
        print(opiniones[0].user.username)
        return opiniones
    except:
        print('No hay opiniones')
    return []

def getOpinionesByUser(username):
    opiniones = Opiniones.objects.all().select_related('user', 'book').filter(user=username)
    return opiniones

def getBookState(username, isbn):
    match = list(Listas.objects.filter(user=username, book=isbn))
    return False if len(match) == 0 else match[0]

def getBookByCoincidence(condition):
    q1 = Libros.objects.filter(isbn__contains=condition)
    q2 = Libros.objects.filter(titulo__contains=condition)
    rs = set(list(q1) +  list(q2))

    return list(rs)

def showBooks(request):
    return render(request, 'libros.html')


def getBooks(_request):
    # Saco los datos de la base de datos
    libros = list(Libros.objects.values())
    # Hago un diccionario con formato JSON e incluyo los libros
    data = {'libros': libros}
    # Devuelvo una respuesta en formato JSON
    return JsonResponse(data)


def showBookDetailsByIsbn(request, isbn):
    libro = Libros.objects.filter(isbn=isbn)
    
    if not libro[0]:
        return HttpResponse('Mal')

    opiniones = getOpinionesByIsbn(isbn)

    if request.user.is_authenticated:
        print('Se supone que esta identificado')
        username = request.user.username
        estado = getBookState(username, isbn)
        if not estado:
            return render(request, 'paginaLibro.html', {'libro': libro[0], 'estado': 'sin_guardar', 'opiniones': opiniones})
        
        return render(request, 'paginaLibro.html', {'libro': libro[0], 'estado': estado.estado, 'opiniones': opiniones})

    return render(request, 'paginaLibro.html', {'libro': libro[0], 'opiniones': opiniones})


def setLista(request=None, operation='', username='', isbn=''):
    print(request.method)
    if request.method == 'POST':
        operation = request.POST.get('operation')
        username = request.POST.get('username')
        isbn = request.POST.get('isbn')
        print(operation, username, isbn)
        if not operation or not username or not isbn:
            print('Uno de los campos no es valido')
            return redirect('/')

        if operation not in ('pendiente', 'leyendo', 'leido', 'sin_guardar'):
            return redirect(f'/libros/getBooks/{isbn}')

        result = getBookState(username, isbn)

        if not result:
            query = Listas.objects.create(
                estado=operation, 
                user=request.user, 
                book=Libros.objects.get(isbn=isbn))
            query.save()
            return redirect(f'/libros/getBooks/{isbn}')

        if result.estado == operation:
            return redirect(f'/libros/getBooks/{isbn}')
        
        result.estado = operation

        result.save()

        return redirect(f'/libros/getBooks/{isbn}')

    else:
        return HttpResponse('No va por POST')

def addOpinion(request=None, opinion='', username='', isbn=''):
    if not request.method == 'POST':
        return HttpResponse('No va por POST')
    
    opinion = request.POST.get('opinion')
    username = request.POST.get('username')
    isbn = request.POST.get('isbn')

    print(opinion)

    if not opinion or not username or not isbn:
        print('Uno de los campos no es valido')
        return redirect('/')



    query = Opiniones.objects.create(
        opinion=opinion, 
        user=request.user, 
        book= Libros.objects.get(isbn=isbn))
    query.save()

    return redirect(f'/libros/getBooks/{isbn}')

    # if result.estado == operation:
    #     return redirect(f'/libros/getBooks/{isbn}')
    
    # result.estado = operation

    # result.save()

    # return redirect(f'/libros/getBooks/{isbn}')

def misLibros(request):
    print(request.user.is_authenticated)
    if not request.user.is_authenticated:
        return redirect('/login')

    username = request.user.username
    libros = getLibrosByUsername(username)

    return render(request, 'misLibros.html', {'res': libros})

def searchBook(request):
    if not request.method == 'POST':
        return HttpResponse('MAL')
        
    condition = request.POST.get('condition')

    libros = getBookByCoincidence(condition=condition)
    return render(request, 'buscarLibro.html', {'matches': libros})
