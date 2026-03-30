import pytest
from django.contrib.auth.models import User
from django.test import Client

from courses.models import Course


@pytest.fixture
def course_data():
    return {
        "title": "Master en Python",
        "content": "<p>Contenido del curso</p>",
        "call_link": "https://example.com/inscripcion",
    }


@pytest.mark.django_db
class TestCourseModel:
    def test_create_course_with_all_fields(self, course_data):
        course = Course.objects.create(**course_data)
        assert course.title == course_data["title"]
        assert course.content == course_data["content"]
        assert course.call_link == course_data["call_link"]
        assert course.show_home is False
        assert bool(course.toc) is False
        assert bool(course.course_image) is False
        assert course.created_at is not None

    def test_course_str_representation(self, course_data):
        course = Course.objects.create(**course_data)
        assert str(course) == course_data["title"]

    def test_course_default_show_home(self):
        course = Course.objects.create(
            title="Test",
            content="Content",
            call_link="https://example.com",
        )
        assert course.show_home is False

    def test_course_without_db(self, course_data):
        course = Course(**course_data)
        assert course.title == course_data["title"]
        assert str(course) == course_data["title"]


@pytest.mark.django_db
class TestCourseViews:
    def test_courses_list_requires_auth(self):
        client = Client()
        response = client.get("/cursos/")
        assert response.status_code == 302
        assert "login" in response.url

    def test_courses_list_shows_courses_authenticated(self):
        User.objects.create_user(
            username="testuser",
            password="testpass123",
        )
        Course.objects.create(
            title="Test Course",
            content="Content",
            call_link="https://example.com",
        )
        client = Client()
        client.login(username="testuser", password="testpass123")
        response = client.get("/cursos/")
        assert response.status_code == 200
        assert "Test Course" in response.content.decode()

    def test_course_detail_requires_auth(self):
        course = Course.objects.create(
            title="Test Course",
            content="Content",
            call_link="https://example.com",
        )
        client = Client()
        response = client.get(f"/cursos/{course.pk}/")
        assert response.status_code == 302
