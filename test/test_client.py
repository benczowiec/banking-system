import re

import pytest

from application.domain.model.client import Client


@pytest.fixture
def client():
    return Client(name="Olga Doe", balance=1000.0)

def test_deposit(client):
    client.deposit(500.0)
    assert client.balance == 1500.0
    assert len(client.transactions) == 1
    assert client.transactions[0].type == "deposit"
    assert client.transactions[0].amount == 500.0

def test_withdraw(client):
    client.withdraw(500.0)
    assert client.balance == 500.0
    assert len(client.transactions) == 1
    assert client.transactions[0].type == "withdraw"
    assert client.transactions[0].amount == 500.0

def test_deposit_raises_error(client):
    with pytest.raises(ValueError, match='Amount must be greater then zero.'):
        client.deposit(-200.0)

def test_withdraw_raises_error(client):
    amount = 2000.0
    message = f"Your current balance ({client.balance}) is smaller than requested withdraw amount ({amount})"
    with pytest.raises(ValueError, match=re.escape(message)):
        client.withdraw(amount)