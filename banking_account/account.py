from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime

class Account(ABC):
    def __init__(self, account_number: int, balance: float, account_type: str):
        self.__account_number = account_number
        self.__balance = balance
        self.__account_type = account_type

    @abstractmethod
    def deposit(self, amount: float) -> None:
        pass

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass

    @abstractmethod
    def transfer(self, destination: 'Account', amount: float) -> None:
        pass

    @abstractmethod
    def show_balance(self) -> None:
        pass

    @abstractmethod
    def get_account_type(self) -> str:
        pass

    def get_balance(self) -> float:
        return self.__balance

    def set_balance(self, amount: float) -> None:
        self.__balance = amount

    def get_account_number(self) -> int:
        return self.__account_number

    def get_account_type(self) -> str:
        return self.__account_type


class CheckingAccount(Account):
    def __init__(self, account_number: int, balance: float, overdraft_limit: float):
        super().__init__(account_number, balance, 'Checking')
        self.__overdraft_limit = overdraft_limit

    def deposit(self, amount: float) -> None:
        self.set_balance(self.get_balance() + amount)

    def withdraw(self, amount: float) -> None:
        if amount <= self.get_balance() + self.__overdraft_limit:
            self.set_balance(self.get_balance() - amount)
        else:
            print("Insufficient funds")

    def transfer(self, destination: Account, amount: float) -> None:
        if amount <= self.get_balance() + self.__overdraft_limit:
            self.withdraw(amount)
            destination.deposit(amount)
        else:
            print("Insufficient funds")

    def show_balance(self) -> None:
        print(f"Checking Account Balance: ${self.get_balance()}")

    def get_account_type(self) -> str:
        return "Checking"


class SavingsAccount(Account):
    def __init__(self, account_number: int, balance: float, interest_rate: float):
        super().__init__(account_number, balance, 'Savings')
        self.__interest_rate = interest_rate

    def deposit(self, amount: float) -> None:
        self.set_balance(self.get_balance() + amount)

    def withdraw(self, amount: float) -> None:
        if amount <= self.get_balance():
            self.set_balance(self.get_balance() - amount)
        else:
            print("Insufficient funds")

    def transfer(self, destination: Account, amount: float) -> None:
        if amount <= self.get_balance():
            self.withdraw(amount)
            destination.deposit(amount)
        else:
            print("Insufficient funds")

    def show_balance(self) -> None:
        print(f"Savings Account Balance: ${self.get_balance()}")

    def get_account_type(self) -> str:
        return "Savings"


class JointAccount(Account):
    def __init__(self, account_number: int, balance: float, joint_owners: List[str]):
        super().__init__(account_number, balance, 'Joint')
        self.__joint_owners = joint_owners

    def add_owner(self, customer_name: str) -> None:
        self.__joint_owners.append(customer_name)

    def deposit(self, amount: float) -> None:
        self.set_balance(self.get_balance() + amount)

    def withdraw(self, amount: float) -> None:
        if amount <= self.get_balance():
            self.set_balance(self.get_balance() - amount)
        else:
            print("Insufficient funds")

    def transfer(self, destination: Account, amount: float) -> None:
        if amount <= self.get_balance():
            self.withdraw(amount)
            destination.deposit(amount)
        else:
            print("Insufficient funds")

    def show_balance(self) -> None:
        print(f"Joint Account Balance: ${self.get_balance()}")

    def get_account_type(self) -> str:
        return "Joint"
