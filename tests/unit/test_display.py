from django.urls import reverse
import pytest
from pytest_django.asserts import assertTemplateUsed

from django.test import TestCase
from django.test.client import RequestFactory

from oc_lettings_site import urls
from oc_lettings_site.views import custom_404, custom_500


def test_database_connection(session):
    # Test to make sure that there are 2 items in the database
    cursor = session
    assert len(list(cursor.execute('SELECT * FROM address'))) == 2


def test_get_index(client):
    response = client.get(reverse('index'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'index.html')


@pytest.mark.django_db
def test_get_lettings_index(client, django_db_setup):
    response = client.get(reverse('lettings_index'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'lettings_index.html')


@pytest.mark.django_db
def test_get_profiles_index(client):
    response = client.get(reverse('profiles_index'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'profiles_index.html')


@pytest.mark.django_db
def test_get_letting_with_id(client, django_db_setup):
    response = client.get(reverse('letting', kwargs={'letting_id': 1}), follow=True)
    assert response.status_code == 200
    assertTemplateUsed(response, 'letting.html')


@pytest.mark.django_db
def test_get_profile(client, django_db_setup):
    response = client.get(reverse('profile', args=("HeadlinesGazer",)), follow=True)
    assert response.status_code == 200
    assertTemplateUsed(response, 'profile.html')


@pytest.mark.django_db
def test_404_page(client, django_db_setup):
    response = client.get("/Unknown")
    assert response.status_code == 404


class TestErrorPages(TestCase):

    def test_error_handlers(self):
        self.assertTrue(urls.handler404.endswith('.custom_404'))
        self.assertTrue(urls.handler500.endswith('.custom_500'))
        factory = RequestFactory()
        request = factory.get('/')
        response = custom_404(request, exception=Exception)
        self.assertEqual(response.status_code, 404)
        self.assertIn('On dirait que tu es perdu...', response.content.decode('UTF8'))
        response = custom_500(request)
        self.assertEqual(response.status_code, 500)
        self.assertIn('Woops', response.content.decode('UTF8'))
