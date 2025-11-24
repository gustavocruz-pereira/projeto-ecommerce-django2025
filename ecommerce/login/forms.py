from django import forms
from django.contrib.auth.models import User

class CriarContaForm(forms.ModelForm):
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Senha', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password2(self):
        senha1 = self.cleaned_data.get("password1")
        senha2 = self.cleaned_data.get("password2")
        if senha1 != senha2:
            raise forms.ValidationError("As senhas não coincidem.")
        return senha2
