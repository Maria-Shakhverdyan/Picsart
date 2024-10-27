from typing import List
from abc import ABC, abstractmethod
from datetime import datetime

class User:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.posts: List['Post'] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if value == "":
            raise ValueError("Name cannot be empty")
        self.__name = value
    
    @property
    def contact_info(self):
        return self.__contact_info

    @contact_info.setter
    def contact_info(self, value):
        if not isinstance(value, str):
            raise TypeError("contact_info must be a string")
        if value == "":
            raise ValueError("contact_info cannot be empty")
        self.__contact_info = value
    
    def create_post(self, content: str, post_type: 'PostType'):
        post = Post(self, content, post_type)
        self.posts.append(post)

    def view_posts(self):
        return [post.post_info() for post in self.posts]
    
    def add_comment(self, post: 'Post', content: str):
        comment = Comment(self, post, content)
        post.add_comment(comment)
    
    def update_profile(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info

class Post:
    def __init__(self, user: User, content: str, post_type: 'PostType'):
        self.user = user
        self.content = content
        self.timestamp = datetime.now()
        self.comments: List['Comment'] = []
        self.post_type = post_type

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, value):
        if not isinstance(value, User):
            raise TypeError("user must be an instance of User")
        self.__user = value
    
    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        if not isinstance(value, str):
            raise TypeError("content must be a string")
        if value == "":
            raise ValueError("content cannot be empty")
        self.__content = value
    
    def add_comment(self, comment: 'Comment'):
        self.comments.append(comment)
    
    def view_comments(self):
        return [comment.comment_info() for comment in self.comments]
    
    def post_info(self):
        return f"Post by {self.user.name}: {self.content} ({self.timestamp})"


class Comment:
    def __init__(self, user: User, post: Post, content: str):
        self.user = user
        self.post = post
        self.content = content
    
    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, value):
        if not isinstance(value, User):
            raise TypeError("user must be an instance of User")
        self.__user = value
    
    @property
    def post(self):
        return self.__post

    @post.setter
    def post(self, value):
        if not isinstance(value, Post):
            raise TypeError("post must be an instance of Post")
        self.__post = value
    
    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        if not isinstance(value, str):
            raise TypeError("content must be a string")
        if value == "":
            raise ValueError("content cannot be empty")
        self.__content = value
    
    def comment_info(self):
        return f"Comment by {self.user.name}: {self.content}"
    
class PostType(ABC):
    @abstractmethod
    def show_post_type(self):
        pass

class TextPost(PostType):
    def show_post_type(self):
        return "Text"

class ImagePost(PostType):
    def show_post_type(self):
        return "Image"


user1 = User("Maria", "maria@example.com")
    
text_post_type = TextPost()
user1.create_post("This is my first post!", text_post_type)
    
image_post_type = ImagePost()
user1.create_post("Check out this photo!", image_post_type)
    
for post_info in user1.view_posts():
    print(post_info)
    
first_post = user1.posts[0]
user1.add_comment(first_post, "Nice post!")
    
for comment_info in first_post.view_comments():
    print(comment_info)
