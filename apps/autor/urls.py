from django.conf.urls import patterns, include, url
from .views import RegistrarAutor, ListarAutor

urlpatterns = patterns('',
    
    url(r'^registrar/$' , RegistrarAutor.as_view(), name="registrar_autor"),
    url(r'^listar/$' , ListarAutor.as_view(), name="listar_autor"),
)