from typing import List
from account import Account

class Customer:
    def __init__(self, name: str, contact_info: str):
        self.__name = name
        self.__contact_info = contact_info
        self.__accounts = []

    def add_account(self, account: Account) -> None:
        self.__accounts.append(account)

    def view_accounts(self) -> None:
        for account in self.__accounts:
            print(f"Account Number: {account.get_account_number()} | Type: {account.get_account_type()} | Balance: ${account.get_balance()}")

    def view_transaction_history(self) -> None:
        print("Viewing transaction history is not implemented yet.")
