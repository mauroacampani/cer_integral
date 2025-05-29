from django.shortcuts import render, redirect
from portal.models import Users, Profesional, Ocupacion, Especialidad
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .form import ProfesionalForm, EspecialidadForm, OcupacionForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View
from portal.form import UserRegisterForm
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.conf import settings
from django.urls import reverse

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
 


class ListProfesional(ListView):
    model = Profesional
    template_name = 'administracion/profesional/listadoProfesional.html'  
    context_object_name = 'profesionales'



class CrearProfesionalView(View):
    def get(self, request):
        user_form = UserRegisterForm()
        profesional_form = ProfesionalForm()
        return render(request, 'administracion/profesional/crearProfesional.html', {
            'user_form': user_form,
            'profesional_form': profesional_form
        })

    def post(self, request):
       
        user_form = UserRegisterForm(request.POST, request.FILES)
        profesional_form = ProfesionalForm(request.POST)
    
        if user_form.is_valid() and profesional_form.is_valid():
            
            user = user_form.save(commit=False)
            user.set_unusable_password()
            user.save()

            profesional = profesional_form.save(commit=False)
            profesional.user = user
            profesional.save()

            
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)

            reset_link = self.request.build_absolute_uri(
                reverse('validate_token', kwargs={'uidb64': uid, 'token': token})
            )

            # Armar y enviar el email
            email_message = EmailMessage(
            subject="Creación de cuenta en el portal del centro de salud",
            body=(
                f"Hola {user.first_name},\n\n"
                "Tu cuenta ha sido creada en el portal del centro de salud. "
                f"Su usuario es: {user.username},\n\n"
                "Por favor, hacé clic en el siguiente enlace para establecer tu contraseña de acceso:\n\n"
                f"{reset_link}\n\n"
                "Una vez establecida tu contraseña, podés iniciar sesión normalmente.\n\n"
                "Saludos."
            ),
            from_email=settings.EMAIL_HOST_USER,
            to=[user.email],
            )
            email_message.send()

            messages.success(request, "Profesional creado correctamente.")
            return redirect('listadoProfesional')  # Ajustá al nombre correcto
        else:
            print("Errores en user_form:", user_form.errors)
            print("Errores en profesional_form:", profesional_form.errors)
        return render(request, 'administracion/profesional/crearProfesional.html', {
            'user_form': user_form,
            'profesional_form': profesional_form
        })