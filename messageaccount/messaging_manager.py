from abc import ABC, abstractmethod
from message import Message
from conversation import Conversation
from typing import List

class MessagingManager(ABC):
    @abstractmethod
    def send_message(self, message: 'Message') -> None:
        pass
    
    @abstractmethod
    def receive_message(self, message: 'Message') -> None:
        pass
    
    @abstractmethod
    def view_conversation_history(self, conversation: 'Conversation') -> List['Message']:
        pass
