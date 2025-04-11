import uuid
from datetime import datetime

from application.domain.model.transaction import Transaction


class Client:
    def __init__(self, name: str, balance: float = 0):
        self.client_id = uuid.uuid4()
        self.name = name
        self._balance = balance
        self.transactions: list[Transaction] = []

    def __repr__(self):
        return f'Client(client_id={repr(self.client_id)} name={repr(self.name)}, balance={repr(self._balance)}, transactions={repr(self.transactions)})'

    def __eq__(self, other):
        if isinstance(other, Client):
            return self.client_id == other.client_id
        return False

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: float):
        self._validate_money_amount(amount)
        transaction = Transaction(self.client_id, 'deposit', amount)
        self.transactions.append(transaction)
        self._balance += amount

    def withdraw(self, amount: float):
        self._validate_money_amount(amount)
        self._check_if_withdraw_is_possible(amount)
        transaction = Transaction(self.client_id, 'withdraw', amount)
        self.transactions.append(transaction)
        self._balance -= amount

    def print_statement(self):
        if not self.transactions:
            print(f'{datetime.now()} No transactions so far.')
        for transaction in self.transactions:
            print(transaction)

    @staticmethod
    def _validate_money_amount(amount: float):
        if amount <= 0:
            raise ValueError('Amount must be greater then zero.')

    def _check_if_withdraw_is_possible(self, amount: float):
        if amount > self.balance:
            raise ValueError(f'Your current balance ({self.balance}) is smaller than requested withdraw amount ({amount})')
