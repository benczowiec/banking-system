import pytest

from application.domain.model.bank import Bank
from application.domain.model.client import Client


@pytest.fixture
def client_1():
    return Client(name="John Doe", balance=100.0)


@pytest.fixture
def client_2():
    return Client(name="Jane Doe", balance=200.0)


@pytest.fixture
def bank():
    return Bank()


def test_add_client(bank, client_1):
    bank.add_client(client_1)
    assert client_1 in bank._clients


def test_add_existing_client_raises_error(bank, client_1):
    bank.add_client(client_1)
    with pytest.raises(ValueError, match=f"Client with ID {client_1.client_id} already exists."):
        bank.add_client(client_1)


def test_remove_client(bank, client_1):
    bank.add_client(client_1)
    bank.remove_client(client_1)
    assert client_1 not in bank._clients


def test_remove_nonexistent_client_raises_error(bank, client_1):
    with pytest.raises(ValueError, match=f"Client with ID {client_1.client_id} doesn't exists."):
        bank.remove_client(client_1)


def test_get_client_by_id(bank, client_1, client_2):
    bank.add_client(client_1)
    bank.add_client(client_2)
    assert bank.get_client_by_id(client_1.client_id) == client_1
    assert bank.get_client_by_id(client_2.client_id) == client_2


def test_get_client_by_invalid_id_returns_none(bank):
    assert bank.get_client_by_id(uuid4()) is None
