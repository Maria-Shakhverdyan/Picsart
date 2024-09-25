from abc import ABC, abstractmethod
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from user import User
    from conversation import Conversation
    
class Message(ABC):
    from user import User
    def __init__(self, sender: 'User', conversation: 'Conversation') -> None:
        self.__sender = sender
        self.__conversation = conversation
        self.__timestamp = datetime.now()

    @abstractmethod
    def display_content(self) -> None:
        pass

    @abstractmethod
    def get_message_type(self) -> str:
        pass

    def get_sender(self) -> 'User':
        return self.__sender
    
    def get_conversation(self) -> 'Conversation':
        return self.__conversation
    
    def get_timestamp(self) -> datetime:
        return self.__timestamp


class TextMessage(Message):
    def __init__(self, sender: 'User', conversation: 'Conversation', content: str) -> None:
        super().__init__(sender, conversation)
        self.__content = content

    def display_content(self) -> None:
        print(f"{self.get_sender().get_name()} (Text): {self.__content}")

    def get_message_type(self) -> str:
        return "Text"


class MultimediaMessage(Message):
    def __init__(self, sender: 'User', conversation: 'Conversation', file_path: str, media_type: str) -> None:
        super().__init__(sender, conversation)
        self.__file_path = file_path
        self.__media_type = media_type

    def display_content(self) -> None:
        print(f"{self.get_sender().get_name()} (Multimedia {self.__media_type}): {self.__file_path}")

    def get_message_type(self) -> str:
        return "Multimedia"
