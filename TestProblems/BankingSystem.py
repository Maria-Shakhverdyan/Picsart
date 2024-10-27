from typing import List
from abc import ABC, abstractmethod

class AccountInterface(ABC):
    @abstractmethod
    def deposit(self, amount: float):
        pass
    
    @abstractmethod
    def withdraw(self, amount: float):
        pass
    
    @abstractmethod
    def transfer(self, target_account, amount: float):
        pass
    
    @abstractmethod
    def account_info(self):
        pass

class Customer:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.accounts: List[AccountInterface] = []
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self.__name = value

    @property
    def contact_info(self):
        return self.__contact_info

    @contact_info.setter
    def contact_info(self, value):
        if not isinstance(value, str):
            raise TypeError("Contact info must be a string")
        self.__contact_info = value

    def add_account(self, account):
        self.accounts.append(account)
    
    def view_accounts(self):
        for account in self.accounts:
            print(account.account_info())

class Operations(ABC):
    def __init__(self, account_number: int, balance: float, account_type: str):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, value):
        if not isinstance(value, int):
            raise TypeError("Account number must be an integer")
        self.__account_number = value

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Balance must be a number")
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value

    @property
    def account_type(self):
        return self.__account_type

    @account_type.setter
    def account_type(self, value):
        if not isinstance(value, str):
            raise TypeError("Account type must be a string")
        self.__account_type = value

    def deposit(self, value: float):
        self.balance += value
    
    def withdraw(self, value: float):
        if value > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= value
    
    def transfer(self, target_account, amount: float):
        self.withdraw(amount)
        target_account.deposit(amount)

class IndividualAccount(Operations, AccountInterface):
    def account_info(self) -> str:
        return f"Individual Account - Account Number: {self.account_number}, Balance: {self.balance}, Type: {self.account_type}"

class JointAccount(Operations, AccountInterface):
    def __init__(self, account_number: int, balance: float, holders: List[str]):
        super().__init__(account_number, balance, "Joint")
        self.holders = holders

    @property
    def holders(self):
        return self.__holders

    @holders.setter
    def holders(self, value):
        if not all(isinstance(holder, str) for holder in value):
            raise TypeError("Holders must be a list of strings")
        self.__holders = value

    def account_info(self) -> str:
        holders_info = ", ".join(self.holders)
        return f"Joint Account - Account Number: {self.account_number}, Balance: {self.balance}, Holders: {holders_info}"

class Transaction:
    def __init__(self, account, transaction_type: str, amount: float):
        self.account = account
        self.transaction_type = transaction_type
        self.amount = amount

    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, value):
        if not isinstance(value, AccountInterface):
            raise TypeError("Account must implement AccountInterface")
        self.__account = value

    @property
    def transaction_type(self):
        return self.__transaction_type

    @transaction_type.setter
    def transaction_type(self, value):
        if value not in ["deposit", "withdraw"]:
            raise ValueError("Invalid transaction type")
        self.__transaction_type = value

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Amount must be a positive number")
        self.__amount = value

    def execute(self):
        if self.transaction_type == "deposit":
            self.account.deposit(self.amount)
            print(f"Deposited {self.amount} to account {self.account.account_number}. New balance: {self.account.balance}")
        elif self.transaction_type == "withdraw":
            self.account.withdraw(self.amount)
            print(f"Withdrew {self.amount} from account {self.account.account_number}. New balance: {self.account.balance}")

class BankSystem:
    def __init__(self):
        self.customers: List[Customer] = []
    
    def add_customer(self, customer: Customer):
        self.customers.append(customer)
    
    def search_customer(self, name: str):
        for customer in self.customers:
            if name == customer.name:
                return customer
        return None

    def transfer_funds(self, sender, receiver, amount: float):
        sender.transfer(receiver, amount)
        print(f"Transferred {amount} from account {sender.account_number} to account {receiver.account_number}")

if __name__ == "__main__":
    bank = BankSystem()

    customer1 = Customer("Maria", "maria@example.com")
    customer2 = Customer("Anna", "anna@example.com")
    bank.add_customer(customer1)
    bank.add_customer(customer2)

    account1 = IndividualAccount(111, 1000, "Checking")
    account2 = IndividualAccount(222, 500, "Savings")
    account3 = JointAccount(333, 2000, ["Maria", "Anna"])

    customer1.add_account(account1)
    customer1.add_account(account3)
    customer2.add_account(account2)
    customer2.add_account(account3)

    customer1.view_accounts()
    customer2.view_accounts()

    transaction1 = Transaction(account1, "deposit", 200)
    transaction1.execute()

    transaction2 = Transaction(account2, "withdraw", 100)
    transaction2.execute()

    bank.transfer_funds(account1, account2, 300)
    customer1.view_accounts()
    customer2.view_accounts()
