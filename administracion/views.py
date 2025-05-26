from django.shortcuts import render, redirect
from portal.models import Users, Profesional, Ocupacion, Especialidad
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .form import ProfesionalForm, EspecialidadForm, OcupacionForm
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.
def index_administracion(request):    
    variable = 'test variable'
    return render(request, 'administracion/index_administracion.html', {'variable': variable})

#VISTA ESPECIALIDAD BASADAS EN CLASE
class ListEspecialidad(ListView):
    model = Especialidad
    template_name = 'administracion/profesional/listadoEspecialidades.html'  
    context_object_name = 'especialidades'  

    
class RegistroEspecialidadView(CreateView):
    model = Especialidad
    form_class = EspecialidadForm
    template_name = 'administracion/profesional/registroEspecialidad.html'
    success_url = reverse_lazy('listadoEspecialidad')

    def form_valid(self, form):
        messages.success(self.request, "Especialidad registrada con éxito.")
        return super().form_valid(form)


class ActualizarEspecialidadView(UpdateView):
    model = Especialidad
    form_class = EspecialidadForm
    template_name = 'administracion/profesional/editarEspecialidad.html'
    success_url = reverse_lazy('listadoEspecialidad')

    def form_valid(self, form):
        messages.success(self.request, "Especialidad editada correctamente.")
        return super().form_valid(form)


class EliminarEspecialidadView(DeleteView):
    model = Especialidad
    template_name = 'administracion/profesional/eliminarEspecialidad.html'
    success_url = reverse_lazy('listadoEspecialidad')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Especialidad eliminada correctamente.")
        return super().delete(request, *args, **kwargs)
    

#VISTA OCUPACION BASADAS EN CLASE
class ListOcupacion(ListView):
    model = Ocupacion
    template_name = 'administracion/profesional/listadoOcupaciones.html'  
    context_object_name = 'ocupaciones' 
 