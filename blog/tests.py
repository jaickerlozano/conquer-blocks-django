import pytest
from django.test import Client

from blog.models import Post


@pytest.fixture
def post_data():
    return {
        "title": "Mi Primer Post",
        "content": "Contenido del post de prueba",
        "author": "Juan Pérez",
    }


@pytest.mark.django_db
class TestPostModel:
    def test_create_post_with_all_fields(self, post_data):
        post = Post.objects.create(**post_data)
        assert post.title == post_data["title"]
        assert post.content == post_data["content"]
        assert post.author == post_data["author"]
        assert post.show_home is False
        assert post.created_at is not None

    def test_post_str_representation(self, post_data):
        post = Post.objects.create(**post_data)
        assert str(post) == post_data["title"]

    def test_post_default_show_home(self):
        post = Post.objects.create(
            title="Test",
            content="Content",
            author="Author",
        )
        assert post.show_home is False

    def test_post_without_db(self, post_data):
        post = Post(**post_data)
        assert post.title == post_data["title"]
        assert str(post) == post_data["title"]


@pytest.mark.django_db
class TestBlogViews:
    def test_blog_list_shows_all_posts(self):
        Post.objects.create(title="Post 1", content="Content", author="Author")
        Post.objects.create(title="Post 2", content="Content", author="Author")
        client = Client()
        response = client.get("/blog/")
        assert response.status_code == 200
        assert "Post 1" in response.content.decode()
        assert "Post 2" in response.content.decode()

    def test_blog_detail_returns_correct_post(self):
        post = Post.objects.create(
            title="Test Post",
            content="Test Content",
            author="Author",
        )
        client = Client()
        response = client.get(f"/blog/{post.pk}/")
        assert response.status_code == 200
        assert "Test Post" in response.content.decode()
        assert "Test Content" in response.content.decode()
