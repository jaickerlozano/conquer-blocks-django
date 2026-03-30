from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, FormView

from blog.models import Post
from courses.models import Course

from .forms import ContactForm, LoginForm, UserRegisterForm
from .models import Contact


class HomeView(TemplateView):
    template_name = 'main_web/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(show_home=True)
        context['posts'] = Post.objects.filter(show_home=True)
        return context


class HomeView2(HomeView):
    template_name = 'main_web/index2.html'


class QuienesSomosView(TemplateView):
    template_name = 'main_web/quienes_somos.html'


class RegistroView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'main_web/registro.html'
    success_url = reverse_lazy('main_web:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        message_content = f'Usuario registrado exitosamente:\nNombre de usuario: {user.username}\nEmail: {user.email}'
        send_mail(
            "Registro exitoso - Conquer Blocks",
            message_content,
            "jlozano.devcode@gmail.com",
            [user.email],
            fail_silently=False,
        )
        return response


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'main_web/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(reverse('main_web:index'))
        else:
            form.add_error(None, "Usuario no válido")
            return self.form_invalid(form)


def logout_view(request):
    logout(request)
    return redirect(reverse('main_web:index'))


class ContactoView(FormView):
    template_name = 'main_web/contacto.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        nombre = form.cleaned_data['name']
        email = form.cleaned_data['email']
        mensaje = form.cleaned_data['message']
        message_content = f"Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}"
        Contact.objects.create(name=nombre, email=email, message=mensaje)
        send_mail(
            "Formulario de contacto - Conquer Blocks",
            message_content,
            "jlozano.devcode@gmail.com",
            [email],
            fail_silently=False,
        )
        return super().form_valid(form)
