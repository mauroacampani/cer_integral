from django import forms
from portal.models import Users
from django.contrib.auth.forms import UserCreationForm

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