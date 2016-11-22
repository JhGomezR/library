from django.views.generic import ListView,CreateView, TemplateView
from django.core.urlresolvers import reverse_lazy
from .models import Autor

# Create your views here.

class RegistrarAutor(CreateView):
	template_name = 'autor/registrarAutor.html'
	model = Autor
	success_url = reverse_lazy('listar_autor')


class ListarAutor(ListView):
	template_name = 'autor/listarAutor.html'
	model = Autor
	context_object_name = 'autors'