from django import forms
from portal.models import Users
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from django.core.exceptions import ValidationError

class UserRegisterForm(forms.ModelForm):
    confirm_email = forms.EmailField(label="Confirmar Email")

    class Meta:
        model = Users
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Users.objects.filter(email=email).exists():
            raise ValidationError("Este correo ya está registrado.")
        return email

    def clean(self):
        
        cleaned_data = super().clean()
       
        email = cleaned_data.get("email")
        confirm_email = cleaned_data.get("confirm_email")
        print(confirm_email)
        if email and confirm_email and email != confirm_email:
            raise ValidationError("Los correos electrónicos no coinciden.")

        return cleaned_data
    


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

    
#FORM EDITAR EL PERFIL DE USUARIOS
class editarUsuarioForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['id', 'username', 'email', 'last_name', 'first_name', 'is_active', 'is_staff']