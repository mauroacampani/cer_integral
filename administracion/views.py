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
    template_name = 'administracion/profesional/especialidad/listadoEspecialidades.html'  
    context_object_name = 'especialidades'  

    
class RegistroEspecialidadView(CreateView):
    model = Especialidad
    form_class = EspecialidadForm
    template_name = 'administracion/profesional/especialidad/registroEspecialidad.html'
    success_url = reverse_lazy('listadoEspecialidad')

    def form_valid(self, form):
        messages.success(self.request, "Especialidad registrada con éxito.")
        return super().form_valid(form)


class ActualizarEspecialidadView(UpdateView):
    model = Especialidad
    form_class = EspecialidadForm
    template_name = 'administracion/profesional/especialidad/editarEspecialidad.html'
    success_url = reverse_lazy('listadoEspecialidad')

    def form_valid(self, form):
        messages.success(self.request, "Especialidad editada correctamente.")
        return super().form_valid(form)


class EliminarEspecialidadView(DeleteView):
    model = Especialidad
    template_name = 'administracion/profesional/especialidad/eliminarEspecialidad.html'
    success_url = reverse_lazy('listadoEspecialidad')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Especialidad eliminada correctamente.")
        return super().delete(request, *args, **kwargs)
    

#VISTA OCUPACION BASADAS EN CLASE
class ListOcupacion(ListView):
    model = Ocupacion
    template_name = 'administracion/profesional/ocupacion/listadoOcupacion.html'  
    context_object_name = 'ocupaciones' 


class RegistroOcupacionView(CreateView):
    model = Especialidad
    form_class = OcupacionForm
    template_name = 'administracion/profesional/ocupacion/registroOcupacion.html'
    success_url = reverse_lazy('listadoOcupacion')

    def form_valid(self, form):
        messages.success(self.request, "Ocupación registrada con éxito.")
        return super().form_valid(form)
    

class ActualizarOcupacionView(UpdateView):
    model = Ocupacion
    form_class = OcupacionForm
    template_name = 'administracion/profesional/ocupacion/editarOcupacion.html'
    success_url = reverse_lazy('listadoOcupacion')

    def form_valid(self, form):
        messages.success(self.request, "Ocupación editada correctamente.")
        return super().form_valid(form)
    

class EliminarOcupacionView(DeleteView):
    model = Ocupacion
    template_name = 'administracion/profesional/ocupacion/eliminarOcupacion.html'
    success_url = reverse_lazy('listadoOcupacion')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Ocupación eliminada correctamente.")
        return super().delete(request, *args, **kwargs)
 