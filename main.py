from banking.bank import Bank
from banking.controller import BankController
from banking.commands import Deposit, Withdrawal, Transfer


def main() -> None:
    bank = Bank()


    # Create a bank controller
    controller = BankController()

    account1 = bank.create_account("Kanak")
    account2 = bank.create_account("CosmicOppai")
    account3 = bank.create_account("The SayAnime")

    controller.execute(Deposit(account1, 500))
    controller.execute(Deposit(account2, 5000))
    controller.execute(Deposit(account3, 50000))

    controller.execute(Withdrawal(account1, 10))
    controller.execute(Withdrawal(account2, 100))
    controller.execute(Withdrawal(account3, 10000))

    controller.execute(Transfer(from_account=account1, to_account=account3, amount=100))
    controller.execute(Transfer(from_account=account2, to_account=account3, amount=400))
    controller.undo()
    print(bank)


if __name__ == "__main__":
    main()