from typing import List
from user import User
from message import Message

class Conversation:
    def __init__(self, participants: List['User'], message_history: List['Message'] = []) -> None:
        self.__participants = participants
        self.__message_history = message_history

    def add_message(self, message: 'Message') -> None:
        self.__message_history.append(message)

    def add_user(self, user: 'User') -> None:
        if user not in self.__participants:
            self.__participants.append(user)

    def get_messages(self) -> List['Message']:
        return self.__message_history

    def get_participants(self) -> List['User']:
        return self.__participants
