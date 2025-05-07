from django import forms
from portal.models import Users
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm

class UserRegisterForm(UserCreationForm):
    
    class Meta:
        model = Users
        fields = ['username', 'password1', 'password2', 'email']
    
    def clean_email(self):
        email1 = self.cleaned_data['email']
    
        email_usuario = Users.objects.filter(email=email1)
        
        if email_usuario:
            raise forms.ValidationError("El email existe")
        return email1
    


class FormReset(forms.ModelForm):
    email = forms.EmailField(required=True, label='Email', widget=forms.TextInput(attrs={
        'placeholder': 'Ingrese su Email',
        'class': 'form-control form-control-sm',
        'autocomplete': 'off',
    }))
    class Meta:
        model = Users
        fields = ['email']
    #email = forms.EmailField(required=True)

    def clean_email(self):
        email1 = self.cleaned_data['email']
        
        email_usuario = Users.objects.filter(email=email1)
        
        if not email_usuario:
            raise forms.ValidationError("El email no existe")
        return email1


#FORM PARA CAMBIAR EL PASSWORD DEL USUARIO
class cambiarPasswordForm(PasswordChangeForm):
    class Meta:
        model = Users
        fields = '__all__'


#FORM EDITAR EL PERFIL DE USUARIOS
class editarPerfilForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'email', 'imagen']
        # widgets = {
        #     'first_name': forms.TextInput(attrs={'class': 'form-control form-control-sm' }),
        #     'last_name': forms.TextInput(attrs={'class': 'form-control form-control-sm' }),
        #     'mail': forms.TextInput(attrs={'class': 'form-control form-control-sm' }),
        #     'imagen': forms.FileInput(attrs={'tipe': 'file', 'class': 'form-control-file form-control-sm'  })
        # }