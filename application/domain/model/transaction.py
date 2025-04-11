from datetime import datetime
from uuid import UUID


class Transaction:
    def __init__(self, client_id: UUID, type: str, amount: float):
        self.client_id = client_id
        self.type = type
        self.amount = amount
        self.date = datetime.now()

    def __str__(self):
        return f'{self.type}, {self.amount:.2f}, {self.date}'

    def __repr__(self):
        return f"Transaction(client_name={repr(self.client_id)}, type={repr(self.type)}, amount={repr(self.amount)}, date={repr(self.date)})"
