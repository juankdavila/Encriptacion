from django.urls import path
from . import views

urlpatterns = [
    path('encriptar/', views.encriptar_texto, name='encriptar_texto'),
]