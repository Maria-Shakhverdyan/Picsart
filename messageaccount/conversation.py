from typing import NewType, List

UserType = NewType('UserType', object)
MessageType = NewType('MessageType', object)
ConversationType = NewType('ConversationType', object)

class Conversation:
    def __init__(self, participants: List[UserType], message_history: List[MessageType] = []) -> None:
        self.__participants = participants
        self.__message_history = message_history

    def add_message(self, message: MessageType) -> None:
        self.__message_history.append(message)

    def add_user(self, user: UserType) -> None:
        if user not in self.__participants:
            self.__participants.append(user)

    def get_messages(self) -> List[MessageType]:
        return self.__message_history

    def get_participants(self) -> List[UserType]:
        return self.__participants
