from django.urls import reverse
import pytest
from pytest_django.asserts import assertTemplateUsed
# from utils import CacheService

def test_dummy():
    assert 1


def test_database_connection(session):
    # Test to make sure that there are 2 items in the database
    cursor = session
    assert len(list(cursor.execute('SELECT * FROM address'))) == 2


def test_get_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assertTemplateUsed(response, 'index.html')
    response = client.get(reverse('index'))


@pytest.mark.django_db
def test_get_lettings_index(client):
    response = client.get('/lettings/')
    print("***************************", response.content)
    assert response.status_code == 200
    assertTemplateUsed(response, 'lettings_index.html')
    response = client.get(reverse('lettings_index'))


@pytest.mark.django_db
def test_get_profiles_index(client):
    response = client.get('/profiles/')
    assert response.status_code == 200
    assertTemplateUsed(response, 'profiles_index.html')
    response = client.get(reverse('profiles_index'))


@pytest.mark.django_db
def test_get_letting(client):
    response = client.get('/lettings/1/')
    # print("***************************", response.content)
    assert response.status_code == 200
    assertTemplateUsed(response, 'letting.html')
    response = client.get(reverse('letting'))


@pytest.mark.django_db
def test_get_profile(client):
    response = client.get('/profiles/HeadlinesGazer/')
    # print("***************************", response.content)
    assert response.status_code == 200
    assertTemplateUsed(response, 'profile.html')
    response = client.get(reverse('profile'))