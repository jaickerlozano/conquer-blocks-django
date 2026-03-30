import pytest
from django.test import Client

from blog.models import Post
from courses.models import Course
from main_web.forms import ContactForm, UserRegisterForm
from main_web.models import Contact


@pytest.fixture
def contact_data():
    return {
        "name": "Juan Pérez",
        "email": "juan@example.com",
        "message": "Este es un mensaje de prueba",
    }


@pytest.mark.django_db
class TestContactModel:
    def test_create_contact_with_all_fields(self, contact_data):
        contact = Contact.objects.create(**contact_data)
        assert contact.name == contact_data["name"]
        assert contact.email == contact_data["email"]
        assert contact.message == contact_data["message"]
        assert contact.contactado is False
        assert contact.created_at is not None

    def test_contact_str_representation(self, contact_data):
        contact = Contact.objects.create(**contact_data)
        expected = f"Contacto de {contact_data['name']} ({contact_data['email']})"
        assert str(contact) == expected

    def test_contact_default_values(self):
        contact = Contact.objects.create(
            name="Test",
            email="test@test.com",
            message="Test message",
        )
        assert contact.contactado is False
        assert contact.created_at is not None

    def test_contact_without_db(self):
        contact = Contact(
            name="Test",
            email="test@test.com",
            message="Test message",
        )
        assert contact.name == "Test"
        assert contact.contactado is False


class TestContactForm:
    def test_valid_contact_form(self):
        form = ContactForm(
            data={
                "name": "Juan Pérez",
                "email": "juan@example.com",
                "message": "Este es un mensaje de prueba",
            }
        )
        assert form.is_valid() is True

    def test_invalid_name_too_short(self):
        form = ContactForm(
            data={
                "name": "Juan",
                "email": "juan@example.com",
                "message": "Este es un mensaje de prueba",
            }
        )
        assert form.is_valid() is False
        assert "name" in form.errors

    def test_invalid_email(self):
        form = ContactForm(
            data={
                "name": "Juan Pérez",
                "email": "not-an-email",
                "message": "Este es un mensaje de prueba",
            }
        )
        assert form.is_valid() is False
        assert "email" in form.errors


@pytest.mark.django_db
class TestUserRegisterForm:
    def test_password_mismatch(self):
        form = UserRegisterForm(
            data={
                "username": "juanperez",
                "first_name": "Juan",
                "last_name": "Pérez",
                "email": "juan@example.com",
                "password1": "TestPass123!",
                "password2": "DifferentPass123!",
            }
        )
        assert form.is_valid() is False
        assert "password2" in form.errors

    def test_valid_registration_form(self):
        form = UserRegisterForm(
            data={
                "username": "juanperez2",
                "first_name": "Juan",
                "last_name": "Pérez",
                "email": "juan2@example.com",
                "password1": "ValidPass123!",
                "password2": "ValidPass123!",
            }
        )
        assert form.is_valid() is True


@pytest.mark.django_db
class TestViews:
    def test_home_view_shows_courses(self):
        Course.objects.create(
            title="Test Course",
            content="Content",
            call_link="https://example.com",
            show_home=True,
        )
        client = Client()
        response = client.get("/")
        assert response.status_code == 200
        assert "Test Course" in response.content.decode()

    def test_home_view_shows_posts(self):
        Post.objects.create(
            title="Test Post",
            content="Content",
            author="Author",
            show_home=True,
        )
        client = Client()
        response = client.get("/")
        assert response.status_code == 200
        assert "Test Post" in response.content.decode()

    def test_contact_view_get(self):
        client = Client()
        response = client.get("/contacto/")
        assert response.status_code == 200

    def test_login_view_get(self):
        client = Client()
        response = client.get("/login/")
        assert response.status_code == 200
