from django.shortcuts import render
from django.contrib import admin
from django.views.generic import View
from django .contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import User

admin.site.register(User)

# class RegistrarUsuario(View):
#     def get(self, request):
#         form = UserCreationForm()
        
#         return render(request, '')
    
#     def post(self, request):
#         form = UserCreationForm()
        
#         usuario = form.save()
        
#         login(request, usuario)
        
