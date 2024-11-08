from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Laboratorio, Producto
from .forms import ProductoForm
from laboratorio.models import Laboratorio, DirectorGeneral, Producto


# Create your views here.
class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'laboratorio/producto_form.html'
    success_url = reverse_lazy('laboratorio:producto_list')

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'laboratorio/producto_form.html'
    success_url = reverse_lazy('laboratorio:producto_list')
    
#---------------------------------------------------------------------------

class LaboratorioListView(ListView):
    model = Laboratorio
    template_name = 'laboratorio/laboratorio_list.html'

class LaboratorioCreateView(CreateView):
    model = Laboratorio
    fields = ['nombre', 'ciudad', 'pais']
    template_name = 'laboratorio/laboratorio_form.html'
    success_url = reverse_lazy('laboratorio:laboratorio_list')

class LaboratorioUpdateView(UpdateView):
    model = Laboratorio
    fields = ['nombre', 'ciudad', 'pais']
    template_name = 'laboratorio/laboratorio_form.html'
    success_url = reverse_lazy('laboratorio:laboratorio_list')

class LaboratorioDeleteView(DeleteView):
    model = Laboratorio
    template_name = 'laboratorio/laboratorio_confirm_delete.html'
    success_url = reverse_lazy('laboratorio:laboratorio_list')

class LaboratorioDetailView(DetailView):
    model = Laboratorio
    template_name = 'laboratorio/laboratorio_detail.html'
    

def pagina_principal(request):
    return render(request, 'laboratorio/pagina_principal.html')

    