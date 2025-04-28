from django.shortcuts import render
from django.contrib import messages
from .models import Users
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from .form import UserRegisterForm

# Create your views here.
def index(request):
    return render(request, 'portal/index.html')


class RegistroUsuarioView(CreateView):
    model = Users
    form_class = UserRegisterForm
    template_name = 'registration/registroUsuario.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        
        usuario = form.save()

        group = Group.objects.get(name='usuario')
        group.user_set.add(usuario)

        messages.add_message(self.request, messages.SUCCESS,
                             "Usuario creado correctamente")

        return super().form_valid(form)