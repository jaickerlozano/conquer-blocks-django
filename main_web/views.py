from django.shortcuts import render
from courses.models import Course
from blog.models import Post
from .forms import ContactForm
from django.core.mail import send_mail


# Create your views here.
def home_view(request):
    # Contexto para la página de inicio.
    context = {
        # Filtra los cursos para mostrar solo los que tienen show_home=True.
        'courses': Course.objects.filter(show_home=True),
        # Filtra los posts para mostrar solo los que tienen show_home=True.
        'posts': Post.objects.filter(show_home=True),
    }
    return render(request, 'main_web/index.html', context)

def quienes_somos_view(request):
    return render(request, 'main_web/quienes_somos.html')

def registro_view(request):
    return render(request, 'main_web/registro.html')

def login_view(request):
    return render(request, 'main_web/login.html')

def contacto_view(request):

    if request.method == 'POST':
        formulario = ContactForm(request.POST)

        if formulario.is_valid():

            nombre = formulario.cleaned_data['name']
            email = formulario.cleaned_data['email']
            mensaje = formulario.cleaned_data['message']

            message_content = f"Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}"

            success = send_mail(
                "Formulario de contacto - Conquer Blocks",
                message_content,
                "info@laveladaconquer.com",
                ["jlozano@gmail.com"],
                fail_silently=False,
            )

            context = {
                'form': formulario,
                'success': success
            }

            print(f'Se ha enviado un correo a {nombre} procedente del email {email} con el siguiente mensaje: {mensaje}')
            return render(request, 'main_web/contacto.html', context)  

        else:
            context = {
                'form': formulario,
            }
            return render(request, 'main_web/contacto.html', context)  
    
    formulario = ContactForm()
    context = {
        'form': formulario
    }   
    return render(request, 'main_web/contacto.html', context)