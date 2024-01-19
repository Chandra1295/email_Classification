import pytest

from app import pancake

@pytest.fixture
def client():
    return pancake.test_client()
