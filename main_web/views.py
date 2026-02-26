from django.shortcuts import render
from courses.models import Course
from blog.models import Post
from .forms import ContactForm
from django.core.mail import send_mail
from .models import Contact


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

    # Si el método de la solicitud es POST, significa que el usuario ha enviado el formulario de contacto.
    if request.method == 'POST':
        # Creamos una instancia del formulario ContactForm con los datos enviados por el usuario (request.POST).
        formulario = ContactForm(request.POST)
        
        # Si el formulario es válido, procesamos los datos y enviamos el correo electrónico.
        if formulario.is_valid():

            # Extraemos los datos limpios del formulario para construir el mensaje de correo electrónico.
            nombre = formulario.cleaned_data['name']
            email = formulario.cleaned_data['email']
            mensaje = formulario.cleaned_data['message']

            # Construir el contenido del mensaje de correo electrónico con los datos del formulario.
            message_content = f"Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}"

            # Guardar el contacto en la base de datos
            Contact.objects.create(
                name=nombre,
                email=email,
                message=mensaje
            )

            # Enviar el correo electrónico con el contenido del formulario
            success = send_mail(
                "Formulario de contacto - Conquer Blocks",
                message_content,
                "info@laveladaconquer.com",
                ["jlozano@gmail.com"],
                fail_silently=False,
            )

            # Preparar el contexto para renderizar la plantilla de contacto, incluyendo el formulario y el resultado del envío del correo.
            context = {
                'form': formulario,
                'success': success
            }

            return render(request, 'main_web/contacto.html', context)  

        else:
            # Si el formulario no es válido, renderizamos la plantilla de contacto nuevamente con el formulario que contiene los errores de validación.
            context = {
                'form': formulario,
            }
            return render(request, 'main_web/contacto.html', context)  
    
    # Si el método de la solicitud no es POST, significa que el usuario está accediendo a la página de contacto por primera vez, por lo que simplemente renderizamos la plantilla con un formulario vacío.
    formulario = ContactForm()
    context = {
        'form': formulario
    }   
    return render(request, 'main_web/contacto.html', context)