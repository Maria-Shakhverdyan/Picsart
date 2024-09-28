from typing import List
from message import Message
from conversation import Conversation

class User:
    def __init__(self, name: str, contact_info: str, conversations: List['Conversation']) -> None:
        self.__name = name
        self.__contact_info = contact_info
        self.__conversations = conversations

    def create_conversation(self, user: 'User') -> 'Conversation':
        from conversation import Conversation
        conversation = Conversation([self, user], [])
        self.__conversations.append(conversation)
        return conversation


    def send_message(self, message: 'Message', conversation: 'Conversation') -> None:
        conversation.add_message(message)

    def receive_message(self, message: 'Message') -> None:
        print(f"Message received by {self.__name}:")
        message.display_content()

    def manage_settings(self) -> None:
        print(f"Managing settings for {self.__name}")

    def get_conversations(self) -> List['Conversation']:
        return self.__conversations

    def get_name(self) -> str:
        return self.__name
    
    def get_contact_info(self) -> str:
        return self.__contact_info
    
