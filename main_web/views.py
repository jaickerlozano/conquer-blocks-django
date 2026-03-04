from django.shortcuts import render, redirect  
from courses.models import Course
from blog.models import Post
from .forms import ContactForm, LoginForm, UserRegisterForm
from django.core.mail import send_mail
from .models import Contact
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User # Importamos el modelo User para crear nuevos usuarios en el registro
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


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

class HomeView(TemplateView):
    template_name = 'main_web/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(show_home=True)
        context['posts'] = Post.objects.filter(show_home=True)
        return context

class HomeView2(HomeView):
    template_name = 'main_web/index2.html'
    

def quienes_somos_view(request):
    return render(request, 'main_web/quienes_somos.html')

class QuienesSomosView(TemplateView):
    template_name = 'main_web/quienes_somos.html'


def registro_view(request):

    if request.user.is_authenticated:
        return redirect(reverse('main_web:index'))

    if request.POST:
        # Procesamos el formulario de registro enviado
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
           
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1
            )

            if user:
                user.first_name = first_name
                user.last_name = last_name
                user.save()
            
            # Construir el contenido del mensaje de correo electrónico con los datos del formulario.
            message_content = f'Usuario registrado exitosamente:\nNombre de usuario: {username}\nEmail: {email}'

            success = send_mail(
                "Registro exitoso - Conquer Blocks",
                message_content,
                "jlozano.devcode@gmail.com",
                [email],
                fail_silently=False,
            )

            context = {
                'msj': "Usuario registrado exitosamente. Ya puedes iniciar sesión.",
                'success': success # esto es por si queremos mostrar un mensaje en la plantilla confirmando que el correo se envió correctamente. No afecta en nada con el envío del correo, es solo para mostrar un mensaje en la plantilla.
            }
            return render(request, 'main_web/registro.html', context)

        else:
            context = {
                'form': form,
                'error': True
            }
            return render(request, 'main_web/registro.html', context)
    else:
        form = UserRegisterForm()
        context = {
            'form': form
        }

        return render(request, 'main_web/registro.html', context)

# Refactorización: Usamos CreateView para simplificar la creación de usuarios.
# CreateView maneja automáticamente el GET (mostrar form) y el POST (validar y guardar).
class RegistroView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'main_web/registro.html'
    success_url = reverse_lazy('main_web:login')

    # form_valid se ejecuta cuando el formulario ha pasado todas las validaciones.
    # Aquí es donde inyectamos lógica extra, como enviar el correo.
    def form_valid(self, form):
        # 1. Llamamos a super().form_valid(form).
        # Esto hace lo más importante: llama a form.save() (creando el usuario en la BD)
        # y devuelve una respuesta de redirección (HttpResponseRedirect) hacia success_url.
        response = super().form_valid(form)
        
        # 2. Accedemos al objeto recién creado.
        # CreateView guarda el objeto creado en self.object automáticamente tras el éxito.
        user = self.object

        # Construir el contenido del mensaje de correo electrónico con los datos del formulario.
        message_content = f'Usuario registrado exitosamente:\nNombre de usuario: {user.username}\nEmail: {user.email}'

        send_mail(
            "Registro exitoso - Conquer Blocks",
            message_content,
            "jlozano.devcode@gmail.com",
            [user.email],
            fail_silently=False,
        )
        
        # 3. Devolvemos la respuesta original (la redirección al login)
        return response

def login_view(request):
    if request.POST:
        # Procesamos el formulario de login enviado
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # authenticate verifica las credenciales contra la base de datos
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Si el usuario es válido, login() crea la sesión del usuario
                login(request, user)
                # Redirigimos a la página de inicio tras el login exitoso
                return redirect(reverse('main_web:index'))
            
            else:
                context = {
                    'form': form,
                    'error': True,
                    'error_message': "Usuario no válido"
                }
                return render(request, 'main_web/login.html', context)

        else:
            context = {
                'form': form,
                'error': True
            }
            return render(request, 'main_web/login.html', context)
    else:
        form = LoginForm()
        context = {
            'form': form
        }

        return render(request, 'main_web/login.html', context)
    
def logout_view(request):
    # logout() cierra la sesión actual y limpia los datos de sesión
    logout(request)
    return redirect(reverse('main_web:index'))



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
                "jlozano.devcode@gmail.com",
                [email],
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

class ContactoView(FormView):
    template_name = 'main_web/contacto.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
    # This method is called when valid form data has been POSTed.
    # It should return an HttpResponse.
        # Extraemos los datos limpios del formulario para construir el mensaje de correo electrónico.
        nombre = form.cleaned_data['name']
        email = form.cleaned_data['email']
        mensaje = form.cleaned_data['message']

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
            "jlozano.devcode@gmail.com",
            [email],
            fail_silently=False,
        )


        return super().form_valid(form)
