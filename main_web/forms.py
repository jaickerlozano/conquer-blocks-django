from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=100)
    email = forms.EmailField(label="Correo electrónico")
    message = forms.CharField(label="Mensaje", widget=forms.Textarea)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 5:
            raise forms.ValidationError("El nombre debe tener al menos 5 caracteres.")
        return name