from uuid import UUID

from application.domain.model.client import Client


class Bank:
    def __init__(self, clients: list[Client] = None):
        self._clients = clients if clients else []

    def __repr__(self):
        return f'Bank(clients={repr(self._clients)})'

    def add_client(self, client: Client):
        if client in self._clients:
            raise ValueError(f"Client with ID {client.client_id} already exists.")
        self._clients.append(client)

    def remove_client(self, client: Client):
        if client not in self._clients:
            raise ValueError(f"Client with ID {client.client_id} doesn't exists.")
        self._clients.remove(client)

    def get_client_with_given_id(self, client_id: UUID) -> Client:
        """Returns the client matching the given client_id."""
        for client in self._clients:
            if client.client_id == client_id:
                return client
        raise ValueError(f"Client with ID {client_id} doesn't exists.")

    def show_balance_info_of_all_clients(self):
        for client in self._clients:
            print(f'{client.name}: {client.balance:.2f}')

