from uuid import UUID

from application.domain.model.bank import Bank


class TransactionService:
    def __init__(self, bank: Bank):
        self._bank = bank

    def deposit_money_for_a_client(self, client_id: UUID, amount: float):
        client = self._bank.get_client_with_given_id(client_id)
        client.deposit(amount)

    def withdraw_money_for_a_client(self, client_id: UUID, amount: float):
        client = self._bank.get_client_with_given_id(client_id)
        client.withdraw(amount)

