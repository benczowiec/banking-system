from uuid import UUID

from application.domain.model.bank import Bank
from application.domain.model.client import Client


class ClientManagementService:
    def __init__(self, bank: Bank):
        self._bank = bank

    def add_client_to_the_bank(self, client_name: str) -> Client:
        client = Client(name=client_name)
        self._bank.add_client(client)
        return client

    def remove_client_from_the_bank(self, client_id: UUID) -> None:
        client = self._bank.get_client_with_given_id(client_id)
        self._bank.remove_client(client)
