import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


def test_shorten_url_success(client):
    response = client.post('/shorten', json={'URL': 'https://google.com'})

    assert response is not None

    assert response.status_code == 201

    data = response.get_json()

    assert 'url' in data

def test_shorten_url_failure(client):
    response = client.post('/shorten', json={})

    assert response.status_code == 400



def test_get_shorten_url_success(client):
    response = client.post('/shorten', json={'URL': 'https://yandex.ru'})

    url = response.get_json()['url']

    short_code = url.split('/')[-1]

    response = client.get(f'/{short_code}')

    assert response.status_code == 302

def test_get_shorten_url_404(client):
    response = client.get('/beng123')

    assert response.status_code == 404


