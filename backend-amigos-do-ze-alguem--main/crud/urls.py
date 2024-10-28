from django.contrib import admin
from django.urls import path, include
from .views import (
    home, salvar, editar, update, delete,
    lista_beneficiarios, salvar_beneficiario, editar_beneficiario,
    update_beneficiario, delete_beneficiario, lista_voluntarios, salvar_voluntario, editar_voluntario,
    update_voluntario, delete_voluntario
)

urlpatterns = [
    path('', home),
    path('salvar/', salvar, name='salvar'),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),

    # Beneficiarios
    path('beneficiarios/', lista_beneficiarios, name='lista_beneficiarios'),
    path('beneficiarios/salvar/', salvar_beneficiario, name='salvar_beneficiario'),
    path('beneficiarios/editar/<int:id>/',
         editar_beneficiario, name='editar_beneficiario'),
    path('beneficiarios/update/<int:id>/',
         update_beneficiario, name='update_beneficiario'),
    path('beneficiarios/delete/<int:id>/',
         delete_beneficiario, name='delete_beneficiario'),

    # Voluntários
    path('voluntarios/', lista_voluntarios, name='lista_voluntarios'),
    path('voluntarios/salvar/', salvar_voluntario, name='salvar_voluntario'),
    path('voluntarios/editar/<int:id>/',
         editar_voluntario, name='editar_voluntario'),
    path('voluntarios/update/<int:id>/',
         update_voluntario, name='update_voluntario'),
    path('voluntarios/delete/<int:id>/',
         delete_voluntario, name='delete_voluntario'),
]
