from django.urls import reverse
import pytest
from pytest_django.asserts import assertTemplateUsed


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
def test_get_lettings_index(client, session):
    cursor = session
    response = client.get('/lettings/')
    print("***************************", response.content)
    assert response.status_code == 200
    assertTemplateUsed(response, 'lettings_index.html')
    response = client.get(reverse('lettings_index'))


@pytest.mark.django_db
def test_get_profiles_index(client):
    response = client.get(reverse('profiles_index'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'profiles_index.html')
    # response = client.get(reverse('profiles_index'))
    

@pytest.mark.django_db
def test_get_letting_with_id(client, session):

    cursor = session
    response = client.get(reverse('letting',kwargs={'letting_id':1}), follow=True)
    assert response.status_code == 200
    # assertTemplateUsed(response, 'letting.html')


@pytest.mark.django_db
def test_get_profile(client, session):
    cursor = session
    response = client.get(reverse('profile',args=("HeadlinesGazer",)), follow=True)
    assert response.status_code == 200
    # assertTemplateUsed(response, 'profile.html')
