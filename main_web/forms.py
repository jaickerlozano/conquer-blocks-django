from django import forms
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=100)
    email = forms.EmailField(label="Correo electrónico")
    message = forms.CharField(label="Mensaje", widget=forms.Textarea)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 5:
            raise forms.ValidationError("El nombre debe tener al menos 5 caracteres.")
        return name

# Formulario simple para capturar credenciales de usuario
class LoginForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario", max_length=150)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    remember_me = forms.BooleanField(label="Recuérdame", required=False)

# Refactorización: Usamos ModelForm en lugar de Form.
# Esto permite vincular el formulario directamente al modelo User de Django.
# Ventaja: Nos ahorra tener que asignar campo por campo en la vista.
class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label="Nombre de usuario", max_length=150)
    first_name = forms.CharField(label="Nombre", max_length=80)
    last_name = forms.CharField(label="Apellidos", max_length=80)
    email = forms.EmailField(label="Email")

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repite la contraseña", widget=forms.PasswordInput)

    # Meta: Define qué modelo usa este formulario y qué campos se guardarán automáticamente.
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2 and password1 != '':
            raise forms.ValidationError("Las contraseñas no coinciden.")
        
        if password2 != '':
            validate_password(password2)
        
        return password2

    # Sobrescribimos el método save para manejar la encriptación de la contraseña.
    # Los ModelForm por defecto guardan los datos tal cual, pero las contraseñas deben ser hasheadas.
    def save(self, commit=True):
        # 1. Obtenemos la instancia del usuario sin guardarla aún en la BD (commit=False)
        user = super().save(commit=False)
        # 2. Encriptamos la contraseña usando el método set_password del modelo User
        user.set_password(self.cleaned_data['password1'])
        # 3. Si commit es True (lo habitual), guardamos definitivamente el usuario en la BD
        if commit:
            user.save()
        return user