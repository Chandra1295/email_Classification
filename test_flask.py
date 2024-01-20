import pytest

from app import pancake

@pytest.fixture
def client():
    return pancake.test_client()


def test_ping(client):
    response=client.get('/ping')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert response.json == {'message': "Pinging Model pancakelication !!!"}

