from dataclasses import dataclass


@dataclass
class Account:
    name: str
    number: str
    balance: str = 0

    def deposit(self, amount: int):
        self.balance += amount

    def withdraw(self, amount: int):
        if self.balance <= amount:
            raise ValueError("Insufficient Funds")
        self.balance -= amount