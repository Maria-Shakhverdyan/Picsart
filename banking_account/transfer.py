from abc import ABC, abstractmethod
from datetime import datetime
from account import Account
from typing import Optional

class TransactionManager(ABC):
    @abstractmethod
    def log_transaction(self, transaction_type: str, amount: float) -> None:
        pass

    @abstractmethod
    def show_transaction_history(self) -> None:
        pass


class Transaction:
    def __init__(self, from_account: 'Account', to_account: Optional['Account'], amount: float, transaction_type: str):
        self.__from_account = from_account
        self.__to_account = to_account
        self.__amount = amount
        self.__transaction_type = transaction_type
        self.__timestamp = datetime.now()

    def log(self) -> None:
        print(f"Transaction: {self.__transaction_type} | Amount: ${self.__amount} | Time: {self.__timestamp}")
