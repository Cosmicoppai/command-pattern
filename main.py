from banking.bank import Bank
from banking.controller import BankController
from banking.commands import Deposit, Withdrawal, Transfer, Batch


def main() -> None:
    bank = Bank()


    # Create a bank controller
    controller = BankController()

    account1 = bank.create_account("Kanak")
    account2 = bank.create_account("CosmicOppai")
    account3 = bank.create_account("The SayAnime")

    controller.execute((Batch(
        commands=[
            Deposit(account1, 500),
            Deposit(account2, 5000),
            Deposit(account3, 50000),
            Withdrawal(account1, 10),
            Withdrawal(account2, 100),
            Withdrawal(account3, 10000),
            Transfer(from_account=account1, to_account=account3, amount=100),
            Transfer(from_account=account2, to_account=account3, amount=400),
        ]
    )))
    print(bank)


if __name__ == "__main__":
    main()