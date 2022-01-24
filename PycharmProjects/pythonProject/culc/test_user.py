import pytest


@pytest.fixture
def get_user():
    return User(name="Vasya", age="40")


def test_user(user):
    assert user.name == "Vasya"