from user import User
from message import Message, TextMessage, MultimediaMessage
from conversation import Conversation

def main():
    user1 = User("Alice", "alice@example.com", [])
    user2 = User("Bob", "bob@example.com", [])
    user3 = User("Charlie", "charlie@example.com", [])

    conversation1 = user1.create_conversation(user2)

    text_message1 = TextMessage(user1, conversation1, "Hello Bob! How are you?")
    user1.send_message(text_message1, conversation1)

    text_message2 = TextMessage(user2, conversation1, "Hi Alice! I'm doing well, thanks.")
    user2.send_message(text_message2, conversation1)

    multimedia_message1 = MultimediaMessage(user2, conversation1, "/path/to/image.jpg", "Image")
    user2.send_message(multimedia_message1, conversation1)

    text_message3 = TextMessage(user1, conversation1, "That's a nice picture, Bob!")
    user1.send_message(text_message3, conversation1)

    conversation2 = user1.create_conversation(user3)

    multimedia_message2 = MultimediaMessage(user1, conversation2, "/path/to/video.mp4", "Video")
    user1.send_message(multimedia_message2, conversation2)

    text_message4 = TextMessage(user3, conversation2, "Great video, Alice! Thanks for sharing.")
    user3.send_message(text_message4, conversation2)

    print("\nConversation History between Alice and Bob:")
    for message in conversation1.get_messages():
        message.display_content()

    print("\nConversation History between Alice and Charlie:")
    for message in conversation2.get_messages():
        message.display_content()

    print("\nAdding Bob to the conversation between Alice and Charlie...")
    conversation2.add_user(user2)

    text_message5 = TextMessage(user2, conversation2, "Hey everyone! I'm joining this conversation.")
    user2.send_message(text_message5, conversation2)

    print("\nUpdated Conversation History between Alice, Charlie, and Bob:")
    for message in conversation2.get_messages():
        message.display_content()

    print("\nUser Settings Management:")
    user1.manage_settings()
    user2.manage_settings()
    user3.manage_settings()

if __name__ == "__main__":
    main()
